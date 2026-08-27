---
lab:
   title: 'Lab 05: Automate and operate'
   description: 'In this lab, you use Microsoft Graph PowerShell for device management, deploy proactive remediations, configure role-based access control with scope tags, review audit logs, and use built-in Intune reports.'
   duration: 100 minutes
   level: 200
   islab: true
   primarytopics:
      - Microsoft Intune
      - Microsoft Graph
      - Microsoft Entra ID
      - Windows
---

# Lab 05: Automate and operate

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With your Intune environment fully deployed (devices enrolled, apps deployed, security policies configured), you now need to implement automation and operational excellence practices. You'll use Microsoft Graph PowerShell for scripted device management, deploy proactive remediations, implement role-based access control (RBAC) with scope tags for delegated administration, configure audit logging, and leverage built-in reporting for operational insights.

By the end of this lab, you'll have:
- Registered an app in Microsoft Entra ID for unattended Graph API automation
- Authenticated with Microsoft Graph PowerShell SDK
- Queried managed devices and policies using Graph API — including filtering by the `Pharmacy` scope tag
- Deployed a proactive remediation script package using a **pilot-first** rollout pattern
- Assigned the **`Pharmacy Helpdesk`** custom role (created in **Lab 01 Exercise 2 Task 6**) to a delegated administrator (**Lee Gu**) and verified end-to-end scope behavior across all Pharmacy-scoped objects created in Labs 02–04
- Reviewed audit logs for admin activity tracking, including Conditional Access policy edits, compliance policy changes, and scope-tag operations
- Used built-in reports to export device and compliance data
- Monitored tenant health and service status

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Completion of **Lab 02** (update rings, feature updates, and compliance policies deployed)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator credentials
- **SEA-DEV1** (enrolled device, Megan Bowen signed in)
- Microsoft Graph PowerShell SDK installed on SEA-DEV1

---

## Exercise 1: Automate with Microsoft Graph PowerShell

### Scenario

Microsoft Graph is a REST API that provides programmatic access to Microsoft 365 services, including Intune. You'll register an application in Microsoft Entra ID for unattended automation, authenticate with the Graph PowerShell SDK, and perform common management tasks via PowerShell.

### Task 1: Install the Microsoft Graph PowerShell SDK

1. On **SEA-DEV1**, open **Terminal (Admin)** (right-click Start → Terminal (Admin); Windows Terminal opens a PowerShell tab by default).

1. On the **Do you want to allow this app to make changes to your device?** prompt, select **Yes**.

1. Install the Microsoft Graph PowerShell SDK:

   ```powershell
   Install-Module Microsoft.Graph -Scope AllUsers -Force
   ```

   > [!NOTE]
   > The Microsoft.Graph module is a meta-package that installs all Graph PowerShell modules. If prompted to install from an untrusted repository, type **Y** and press Enter.

1. Verify the installation:

   ```powershell
   Get-Module -Name Microsoft.Graph.* -ListAvailable
   ```

   The output should show multiple Microsoft.Graph.* modules (e.g., Microsoft.Graph.Authentication, Microsoft.Graph.Intune, Microsoft.Graph.Users).

**You have successfully installed the Microsoft Graph PowerShell SDK.**

---

### Task 2: Register an application for unattended automation

For interactive automation, you can use delegated permissions (user signs in). For unattended automation (e.g., scheduled scripts), you need application permissions and a client secret or certificate.

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://entra.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Entra admin center**, in the left navigation, expand **Entra ID** and select **App registrations**.

   > [!NOTE]
   > In the current Entra portal, **App registrations** is a direct child of **Entra ID** — there's no "Applications" parent node. (The older "Identity → Applications → App registrations" path no longer exists.)

1. Select **+ New registration**.

1. On the **Register an application** page, enter:
   - **Name:** `Intune Automation App`
   - **Supported account types:** Single tenant only - Contoso (the default; this is the modern label for "Accounts in this organizational directory only")
   - **Redirect URI:** Leave blank

1. Select **Register**.

1. On the **Intune Automation App** overview page, note the following:
   - **Application (client) ID:** (copy this value—you'll need it for authentication)
   - **Directory (tenant) ID:** (copy this value)

**You have successfully registered an application for Graph API access.**

---

### Task 3: Grant API permissions to the application

1. In the **Intune Automation App** details, select **API permissions** from the left navigation.

1. Select **+ Add a permission**.

1. In the **Request API permissions** pane, select **Microsoft Graph**.

1. Select **Application permissions** (not Delegated permissions).

1. Search for and select the following permissions:
   - **DeviceManagementManagedDevices.Read.All** (read device information)
   - **DeviceManagementRBAC.Read.All** (read Intune role-based access control data)
   - **DeviceManagementConfiguration.ReadWrite.All** (read/write configuration policies)
   - **DeviceManagementApps.ReadWrite.All** (read/write applications)
   - **Group.Read.All** (read directory groups — required by `Get-MgGroup` in Task 8)

   > [!NOTE]
   > Application permissions run with the application's identity, not the user's identity. They are suitable for unattended automation but require admin consent.

1. Select **Add permissions**.

1. On the **Intune Automation App | API permissions** page, select **Grant admin consent for Contoso**.

1. In the confirmation dialog, select **Yes**.

1. Verify all permissions show a green checkmark under **Status** (indicating admin consent granted).

**You have successfully granted API permissions to the application.**

---

### Task 4: Create a client secret

1. In the **Intune Automation App** details, select **Certificates & secrets** from the left navigation.

1. Under **Client secrets**, select **+ New client secret**.

1. In the **Add a client secret** pane, enter:
   - **Description:** `Automation secret for PowerShell scripts`
   - **Expires:** 6 months (or 12 months, depending on your policy)

1. Select **Add**.

1. **Immediately copy the secret value** (the long alphanumeric string under **Value**).

   > [!WARNING]
   > The client secret is only displayed once. If you lose it, you must generate a new secret.

1. Save the secret securely (e.g., in Azure Key Vault or a password manager). For lab purposes, save it in a text file on SEA-DEV1 (e.g., `C:\LabScripts\ClientSecret.txt`).

**You have successfully created a client secret for unattended authentication.**

---

### Task 5: Authenticate with Microsoft Graph using application credentials

1. On **SEA-DEV1**, open **Windows PowerShell** (Admin).

1. Create a folder for automation scripts:

   ```powershell
   New-Item -Path "C:\LabScripts" -ItemType Directory -Force
   ```

1. Create and save the authentication script to `C:\LabScripts\Connect-GraphApp.ps1`. First replace `<Your Tenant ID>`, `<Your Application (client) ID>`, and `<Your Client Secret>` between the single quotes with the values you copied earlier, then run the following to write the file:

   ```powershell
   @'
   $tenantId = "<Your Tenant ID>"
   $clientId = "<Your Application (client) ID>"
   $clientSecret = "<Your Client Secret>"

   # Convert client secret to secure string
   $secureSecret = ConvertTo-SecureString $clientSecret -AsPlainText -Force

   # Create credential object
   $credential = New-Object System.Management.Automation.PSCredential ($clientId, $secureSecret)

   # Connect to Microsoft Graph
   Connect-MgGraph -TenantId $tenantId -ClientSecretCredential $credential

   # Verify connection
   Get-MgContext
   '@ | Out-File -FilePath "C:\LabScripts\Connect-GraphApp.ps1" -Encoding UTF8
   ```

   > [!NOTE]
   > The single-quoted here-string (`@'...'@`) writes the `$tenantId`, `$clientId`, and other variables to the file **literally** instead of expanding them now.

1. Change to the script folder, then run the script:

   ```powershell
   cd C:\LabScripts
   .\Connect-GraphApp.ps1
   ```

1. Verify the connection by reviewing the output of `Get-MgContext`:
   - **TenantId:** Should match your tenant ID
   - **Scopes:** Should show the granted application permissions
   - **AuthType:** Should show "AppOnly"

**You have successfully authenticated to Microsoft Graph using application credentials.**

---

### Task 6: Query managed devices using Graph PowerShell

1. In the PowerShell session (with Graph connected), query all managed devices:

   ```powershell
   Get-MgDeviceManagementManagedDevice | Select-Object DeviceName, OperatingSystem, ComplianceState, LastSyncDateTime
   ```
   
1. Review the output. You should see SEA-DEV1 and SEA-DEV2 listed with their compliance status.

1. Query devices with specific filters:

   ```powershell
   # Get devices running Windows
   Get-MgDeviceManagementManagedDevice -Filter "operatingSystem eq 'Windows'" | Select-Object DeviceName, OperatingSystem

   # Get non-compliant devices
   Get-MgDeviceManagementManagedDevice -Filter "complianceState eq 'noncompliant'" | Select-Object DeviceName, ComplianceState
   ```

1. Query the configuration profiles tagged with the `Pharmacy` scope tag (created in **Lab 01 Exercise 2 Task 6** and applied to profiles in **Labs 02–04**). This is the canonical Graph-PowerShell way to enumerate everything a delegated admin (Pharmacy Helpdesk) would see.

   > [!NOTE]
   > The `roleScopeTags` collection is exposed only via the **beta** Graph endpoint at the time of writing, so this lookup uses `Invoke-MgGraphRequest` directly rather than a typed `Get-Mg*` cmdlet:

   ```powershell
   # Resolve the Pharmacy scope tag's numeric ID via the beta endpoint
   $tagsResp = Invoke-MgGraphRequest -Method GET -Uri 'https://graph.microsoft.com/beta/deviceManagement/roleScopeTags'
   $pharmacyTag = $tagsResp.value | Where-Object { $_.displayName -eq 'Pharmacy' }
   if ($pharmacyTag) {
       Write-Output "Pharmacy scope tag ID: $($pharmacyTag.id)"
   } else {
       Write-Output "Pharmacy scope tag not found - confirm it was created in Lab 01 Exercise 2 Task 6"
   }

   # List all device configuration profiles that include the Pharmacy scope tag
   Get-MgDeviceManagementDeviceConfiguration -All |
       Where-Object { $_.AdditionalProperties.roleScopeTagIds -contains $pharmacyTag.id } |
       Select-Object DisplayName, Id

   # List all compliance policies tagged Pharmacy
   Get-MgDeviceManagementDeviceCompliancePolicy -All |
       Where-Object { $_.AdditionalProperties.roleScopeTagIds -contains $pharmacyTag.id } |
       Select-Object DisplayName, Id
   ```

   > [!NOTE]
   > The Graph API surfaces scope tag membership on a per-object basis via the `roleScopeTagIds` array. This is the underlying field the Intune admin center reads when it filters what a delegated admin sees. Querying it directly via Graph is how you'd build a compliance dashboard scoped to a delegated team — or audit which policies a particular scope tag is applied to.

**You have successfully queried managed devices and Pharmacy-scoped policies using Microsoft Graph PowerShell.**

---

### Task 7: Create a compliance policy using Graph API

You'll create a Windows compliance policy using the Graph API (instead of the Intune admin center).

1. In the PowerShell session, define the compliance policy JSON payload. Note the **`scheduledActionsForRule`** block at the end — the Graph API requires every compliance policy to have **exactly one** block action, so this nested object is mandatory:

   ```powershell
   $compliancePolicyJson = @"
   {
     "@odata.type": "#microsoft.graph.windows10CompliancePolicy",
     "displayName": "Graph API - Windows Compliance Policy",
     "description": "Compliance policy created via Microsoft Graph PowerShell",
     "passwordRequired": true,
     "passwordBlockSimple": true,
     "passwordMinimumLength": 8,
     "passwordRequiredType": "alphanumeric",
     "osMinimumVersion": "10.0.19041",
     "bitLockerEnabled": true,
     "secureBootEnabled": true,
     "codeIntegrityEnabled": true,
     "storageRequireEncryption": true,
     "scheduledActionsForRule": [
       {
         "ruleName": "PasswordRequired",
         "scheduledActionConfigurations": [
           {
             "actionType": "block",
             "gracePeriodHours": 0,
             "notificationTemplateId": "",
             "notificationMessageCCList": []
           }
         ]
       }
     ]
   }
   "@
   ```

   > [!IMPORTANT]
   > The properties available on **`windows10CompliancePolicy`** in v1.0 are limited to Windows-device-health attestation settings (BitLocker, Secure Boot, Code Integrity, password rules, storage encryption). Firewall, antivirus, and Defender-related properties live on `windows10MobileCompliancePolicy` or require beta-only types. The full v1.0 property list is at [Microsoft Graph → Create windows10CompliancePolicy](https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10compliancepolicy-create?view=graph-rest-1.0).

1. Create the policy using the Graph API:

   ```powershell
   Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies" -Body $compliancePolicyJson -ContentType "application/json"
   ```

1. Verify the policy was created:

   ```powershell
   Get-MgDeviceManagementDeviceCompliancePolicy | Where-Object { $_.DisplayName -eq "Graph API - Windows Compliance Policy" } | Select-Object DisplayName, Description, Id
   ```

**You have successfully created a compliance policy using the Microsoft Graph API.**

---

### Task 8: Assign the compliance policy to a group

1. Get the policy ID:

   ```powershell
   $policy = Get-MgDeviceManagementDeviceCompliancePolicy | Where-Object { $_.DisplayName -eq "Graph API - Windows Compliance Policy" }
   $policyId = $policy.Id
   ```

1. Get the target group ID (e.g., dyn-Windows-Devices):

   ```powershell
   $group = Get-MgGroup -Filter "displayName eq 'dyn-Windows-Devices'"
   $groupId = $group.Id
   ```

1. Create the assignment JSON payload. Note the `assignments` array wrapper \u2014 the `/assign` action accepts a collection, not a single assignment object:

   ```powershell
   $assignmentJson = @"
   {
     "assignments": [
       {
         "target": {
           "@odata.type": "#microsoft.graph.groupAssignmentTarget",
           "groupId": "$groupId"
         }
       }
     ]
   }
   "@
   ```

1. Assign the policy to the group using the **`/assign`** action endpoint (not `/assignments`):

   ```powershell
   Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies/$policyId/assign" -Body $assignmentJson -ContentType "application/json"
   ```

   > [!NOTE]
   > Compliance-policy assignment is a Graph **action** (`/assign`) rather than a sub-collection POST (`/assignments`). The action takes the full assignment set and replaces any existing assignments \u2014 useful for idempotent automation scripts.

1. Verify the assignment in the Intune admin center:
   - Navigate to **Devices** → **Compliance** → **Graph API - Windows Compliance Policy** → **Properties**

**You have successfully assigned a compliance policy to a group using Microsoft Graph API.**

---

## Exercise 2: Deploy proactive remediations

### Scenario

Proactive remediations automatically detect and fix common device issues before users report them. The upper-intermediate pattern for any new remediation script is a **pilot-first rollout**: deploy to the pilot cohort, watch for detection-vs-remediation outcomes for a day or two, then expand to the broader fleet. You'll follow that pattern here — the same pilot group (`sg-Intune-Pilot-Users`) that received the blocking ESP (Lab 01), the Pilot update ring (Lab 02), and Block-mode ASR (Lab 04) gets the new remediation first.

### Task 1: Create detection and remediation scripts

1. On **SEA-DEV1**, create a folder for remediation scripts:

   ```powershell
   New-Item -Path "C:\LabScripts\Remediations" -ItemType Directory -Force
   ```

1. Create the detection script (`Detect-StaleWindowsUpdateCache.ps1`):

   ```powershell
   @"
   # Detection script: Check for Windows Update cache files older than 30 days
   `$updateCachePath = "C:\Windows\SoftwareDistribution\Download"
   `$oldFiles = Get-ChildItem -Path `$updateCachePath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { `$_.LastWriteTime -lt (Get-Date).AddDays(-30) }

   if (`$oldFiles.Count -gt 0) {
       Write-Output "Found `$(`$oldFiles.Count) stale Windows Update cache files"
       exit 1  # Issue detected
   } else {
       Write-Output "Windows Update cache is clean"
       exit 0  # Compliant
   }
   "@ | Out-File -FilePath "C:\LabScripts\Remediations\Detect-StaleWindowsUpdateCache.ps1" -Encoding UTF8
   ```

1. Create the remediation script (`Remediate-StaleWindowsUpdateCache.ps1`):

   ```powershell
   @"
   # Remediation script: Clear stale Windows Update cache files
   `$updateCachePath = "C:\Windows\SoftwareDistribution\Download"
   try {
       Stop-Service -Name wuauserv -Force -ErrorAction SilentlyContinue
       Get-ChildItem -Path `$updateCachePath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { `$_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item -Force -ErrorAction SilentlyContinue
       Start-Service -Name wuauserv -ErrorAction SilentlyContinue
       Write-Output "Stale Windows Update cache cleared"
       exit 0  # Success
   } catch {
       Write-Error "Failed to clear Windows Update cache: `$_"
       exit 1  # Failure
   }
   "@ | Out-File -FilePath "C:\LabScripts\Remediations\Remediate-StaleWindowsUpdateCache.ps1" -Encoding UTF8
   ```

**You have successfully created detection and remediation scripts.**

---

### Task 2: Upload the remediation script package to Intune

1. In **Microsoft Edge**, navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. Navigate to **Tenant administration** → **Connectors and tokens** → **Windows data**.

1. Expand **Windows data** and set **Enable features that require Windows diagnostic data in processor configuration** to **On**. Expand **Windows license verification** and set **I confirm that my tenant owns one of these licenses** to **On**.

1. In the **Microsoft Intune admin center**, select **Devices**, and then select **Scripts and remediations**.

1. Select the **Remediations** tab.

1. Select **+ Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Remediation - Clear Stale Windows Update Cache`
   - **Description:** `Detects and removes Windows Update cache files older than 30 days`

1. Select **Next**.

1. On the **Settings** tab, configure:
   - **Detection script file:** Browse and select `C:\LabScripts\Remediations\Detect-StaleWindowsUpdateCache.ps1`
   - **Remediation script file:** Browse and select `C:\LabScripts\Remediations\Remediate-StaleWindowsUpdateCache.ps1`
   - **Run this script using the logged on credentials:** No (run as SYSTEM)
   - **Enforce script signature check:** No
   - **Run script in 64-bit PowerShell:** Yes

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Assign to**, select **+ Select groups to include**.

1. Search for and select **sg-Intune-Pilot-Users** (the pilot cohort from Lab 01 — you'll expand to the fleet in Task 4 after watching detection-vs-remediation results).

1. Select **Select**.

1. Select **Next** → **Create**.

**You have successfully uploaded the proactive remediation script package and assigned it to the pilot cohort.**

---

### Task 3: Monitor remediation execution

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Stale Windows Update Cache**.

1. Select **Device status** from the left navigation.

1. Wait 10–15 minutes for the remediation to run on devices.

   > [!NOTE]
   > Remediations run on a schedule (default: once per day). For faster testing, you can force a device sync or wait for the next sync cycle.

1. Review the device status:
   - **Detection status:** Shows whether the issue was detected (exit code 1) or not detected (exit code 0)
   - **Remediation status:** Shows whether the remediation succeeded (exit code 0) or failed (exit code 1)
   - **Last check-in:** Timestamp of last script execution

**You have successfully deployed and monitored a proactive remediation script.**

---

### Task 4: Expand the remediation from pilot to fleet

Once the pilot device status (Task 3) shows the detection script running cleanly (no false positives) and the remediation script succeeding (no script errors), you expand the assignment to the broader fleet. This is the canonical *pilot → fleet* rollout for any new remediation script.

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Stale Windows Update Cache**.

1. Select **Properties** from the left navigation, then in the **Assignments** section select **Edit**.

1. Add a second assignment under **Assign to** → **+ Select groups to include**, and select **dyn-Windows-Devices**. Remove the **sg-Intune-Pilot-Users** group from the included groups. Under **Exclude groups**, select **+ Select groups to exclude** and add **sg-Intune-Pilot-Users** (Pilot already has it; no need to assign twice).

1. Select **Review + save** → **Save**.

   > [!NOTE]
   > A real production rollout would let the pilot run for 24–72 hours before this step, and you'd want to be confident the detection script's exit-code-1 rate matches the actual issue rate (i.e., no false positives) and the remediation succeeded every time it ran. For this lab, you're simulating the rollout flow.

**You have successfully expanded the remediation from pilot to the broader fleet.**

---

## Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end

### Scenario

In **Lab 01 Exercise 2 Task 6** you created the **`Pharmacy Helpdesk`** custom Intune role and the **`Pharmacy`** scope tag. In **Labs 02–04** you applied the `Pharmacy` scope tag to configuration profiles (Lab 02 Ex 1–2), a compliance policy (Lab 02 Ex 2), the pilot update ring (Lab 02 Ex 4), a Win32 LOB app (Lab 03 Ex 2), the Defender security baseline + Antivirus + ASR (Lab 04 Ex 2), and the BitLocker policy (Lab 04 Ex 3). Now you'll **assign** the role to a delegated administrator (**Lee Gu**, `LeeG@<TenantPrefix>.OnMicrosoft.com`), then **sign in as Lee Gu** and verify end-to-end that the delegated admin sees only Pharmacy-scoped objects — not the whole tenant.

This is the culmination of Thread A across the whole lab series. By the end of this exercise, Lee Gu can manage Pharmacy clinical policies but is invisibly walled off from the rest of the tenant.

### Task 1: Review the `Pharmacy Helpdesk` role and `Pharmacy` scope tag

1. In the **Microsoft Intune admin center**, select **Tenant administration** and select **Roles**.

1. Select **All roles**. Locate and select **Pharmacy Helpdesk** (created in **Lab 01 Exercise 2 Task 6**). 

1. Select **Properties** from the left navigation.

1. Select **Edit** next to **Permissions**.

1. Review the **Permissions** tab. Confirm the permissions are set correctly:
   - **Managed devices:** Read, Set primary user, Update = **Yes**; Delete and Wipe = **No**
   - **Remote tasks:** Sync devices, Reboot now, Collect diagnostics = **Yes**
   - **Organization:** Read = **Yes**
   - **Roles:** Read = **Yes**
   - **Device compliance policies**, **Device configurations**, **Managed apps**, **Mobile apps**, **Endpoint Protection Reports**, **Security baselines:** Read = **Yes**; Create, Update, Delete, and Assign = **No**
   - **Remote Help app**: Take full control = **Yes**; View screen = **Yes**; 

   > [!NOTE]
   > This is the principle-of-least-privilege role you defined in Lab 01: enough to operate devices day-to-day, but no authority to change policy. The Pharmacy Helpdesk can sync a device, force a restart, or collect diagnostics — but can't author or delete the compliance policy that says "BitLocker must be on."

1. Go back to **Pharmacy Helpdesk | Properties** and confirm the **Pharmacy** scope tag is listed under **Scope tags**.

1. Navigate back to **Tenant administration** → **Roles** → **Scope tags** and select **Pharmacy**. On the **Scope tag Pharmacy** page, review the **Basics** section (name and description) and the **Assignments** section, which lists the groups the scope tag is assigned to.

**You have successfully reviewed the role and scope tag created in Lab 01.**

---

### Task 2: Inventory the Pharmacy-tagged objects across the lab series

Before assigning the role, confirm which objects Lee Gu will gain visibility to. This matches the Graph PowerShell query you ran in **Exercise 1 Task 6**, now in the portal UI.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Manage devices** → **Configuration**.

1. In the policy list, look for the **Scope tags** column (add it via the column picker if it's not visible). Filter or scroll to find policies showing **Pharmacy** in the Scope tags column. Expected: Settings Catalog and Device Restrictions profiles from **Lab 02 Exercise 1**, and the camera disabled profile if you kept it from the conflict resolution.

1. Navigate to **Devices** → **Manage devices** → **Compliance**. Confirm `Compliance - Windows Security Baseline` shows **Pharmacy**.

1. Navigate to **Apps** → **All apps**. Select `7-Zip Portable` and `7-Zip Portable v2.0` (or your custom portable apps) and select **Properties**. Confirm the **Scope tags** section shows **Pharmacy**.

1. Navigate to **Endpoint security**. Select each option separately: **Security baselines**, **Antivirus**, **Attack surface reduction**, and **Disk encryption**. Confirm `Security Baseline - Defender for Endpoint`, `Antivirus - Defender Configuration`, `ASR - Block (Pilot)`, and the `BitLocker - Full Disk Encryption` policy all have **Pharmacy** listed in their **Scope tags**.

   > [!NOTE]
   > If any expected object doesn't show **Pharmacy**, go back to that lab's exercise and add the scope tag (it's never too late — scope tags are editable after the fact via the policy **Properties** → **Scope tags** → **Edit**).

**You have successfully inventoried the Pharmacy-tagged objects.**

---

### Task 3: Assign the `Pharmacy Helpdesk` role to Lee Gu

   > [!IMPORTANT]
   > Intune role assignments accept **security groups only** — you can't add an individual user directly on the **Admin Groups** or **Scope (Groups)** tabs. So you first create a security group, add Lee Gu as a member, then assign that group to the role.

1. In the **Microsoft Intune admin center**, navigate to **Groups** → **All groups**.

1. Select **+ New group** and enter:
   - **Group type:** Security
   - **Group name:** `sg-Pharmacy-Helpdesk-Admins`
   - **Membership type:** Assigned

1. Under **Members**, select **No members selected**. Search for and select **Lee Gu** (`LeeG@<TenantPrefix>.OnMicrosoft.com`), then select **Select**.

1. Select **Create**.

1. Navigate to **Tenant administration** → **Roles** → **All roles**.

1. Select **Pharmacy Helpdesk**.

1. Select **Assignments** from the left navigation.

1. Select **+ Assign**.

1. On the **Basics** page, enter:
   - **Assignment name:** `Pharmacy Helpdesk - Lee Gu`
   - **Description:** `Grants Lee Gu Pharmacy-scoped helpdesk access`

1. Select **Next**.

1. On the **Admin Groups** tab, select **Add groups**.

   > [!NOTE]
   > The Admin Groups tab defines *who* holds the role. Because it accepts groups only, you assign `sg-Pharmacy-Helpdesk-Admins` (which contains Lee Gu) rather than Lee Gu directly.

1. Search for and select **sg-Pharmacy-Helpdesk-Admins**.

1. Select **Select**, then **Next**.

1. On the **Scope Groups** tab, select **Add groups** and add **dyn-Windows-Devices** (the device target for Pharmacy operations). Select **Select**, then **Next**.

1. On the **Scope Tags** tab, select **+ Select scope tags** and choose **Pharmacy**. Select **Select**.

   > [!IMPORTANT]
   > **Scope (Tags) is what makes the role actually scoped.** Without a scope tag on the assignment, Lee Gu would see all objects in the device target group. The scope tag intersects with the role's permissions and the assignment's group target to produce the final visibility — only Pharmacy-tagged objects that are also in dyn-Windows-Devices.

1. Select **Next** → **Create**.

**You have successfully assigned the Pharmacy Helpdesk role to Lee Gu.**

---

### Task 4: Sign in as Lee Gu and verify scoped visibility end-to-end

This is the moment of truth for Thread A. You'll sign in as Lee Gu and confirm that the entire Pharmacy-scoped chain you built across Labs 01–04 is visible — and that nothing else is.

1. Open a new **InPrivate** or **Incognito** browser window.

1. Navigate to **https://intune.microsoft.com**.

1. Sign in as **LeeG@<TenantPrefix>.OnMicrosoft.com**. Use Lee Gu's password (provided in the lab credentials handout).

   > [!NOTE]
   > If Lee Gu hasn't completed MFA setup, you'll be prompted to enroll. Complete the Authenticator setup. The Conditional Access policy from **Lab 02 Exercise 2** in Report-only mode (or enforced after **Lab 04 Exercise 6**) does not block Lee Gu because Lee isn't in `sg-Intune-Pilot-Users`.

1. In the Intune admin center as Lee Gu, navigate to **Devices** → **Manage devices** → **Configuration**.

1. Confirm Lee Gu sees **only** the configuration profiles tagged with **Pharmacy**. Some profiles tagged with **Default** only (the Feature update profile, Expedited Quality update policy) should **not** appear in Lee Gu's view.

1. Navigate to **Devices** → **Manage devices** → **Compliance**. Confirm `Compliance - Windows Security Baseline` is visible; no other compliance policies appear.

1. Navigate to **Apps** → **All apps**. Confirm `7-Zip Portable` and `7-Zip Portable v2.0` (or your custom portable apps) are visible; Microsoft 365 Apps, Microsoft To Do, Google Chrome (Default-tagged) do **not** appear.

1. Navigate to **Endpoint security** → **Security baselines** / **Antivirus** / **Attack surface reduction** / **Disk encryption**. Confirm only the Pharmacy-tagged policies are visible.

1. Try to **edit** the `Antivirus - Defender Configuration` policy:
   - Open the policy.
   - Scroll to **Properties** → attempt to select **Edit** on the Settings section.
   - The Edit button should be grayed out, unavailable, or selecting it returns an authorization error. Lee Gu's role grants **Read** on compliance policies but not **Create/Update/Delete**.

   > [!NOTE]
   > **You've just proven that Lee Gu can see and audit Pharmacy clinical policies, sync devices, and run remote tasks — but cannot edit or delete policy.** That's exactly the upper-intermediate delegation pattern: scoped visibility + bounded write authority. The Pharmacy Helpdesk handles day-to-day device operations; central IT (Jordan Chen, Global Admin) retains policy authorship.

1. Try **Remote Help** (you'll enable and exercise this fully in **Lab 06 Exercise 2**): in the Intune admin center as Lee Gu, navigate to **Tenant administration** → **Remote Help**. Lee Gu sees **"You don't have access"**.

1. Sign out of the InPrivate window and return to your Jordan Chen admin session.

**You have successfully verified end-to-end that the Pharmacy Helpdesk role + Pharmacy scope tag delegation works exactly as designed across the entire lab series.**

---

## Exercise 4: Monitor audit logs and operational health

### Scenario

Audit logs track administrative actions in Intune, providing accountability and troubleshooting insights. You'll review audit logs and configure diagnostic settings to route logs to Azure Monitor (conceptual).

### Task 1: Review audit logs

1. In the **Microsoft Intune admin center**, select **Tenant administration**, and then select **Audit logs**.

1. On the **Audit logs** page, review the list of recent administrative actions:
   - **Activity:** Type of action (Create, Update, Delete, Assign, etc.)
   - **Date:** Timestamp of the action
   - **Initiated by (actor):** User or service principal who performed the action
   - **Target(s):** Object that was modified (policy, device, app, etc.)

1. Filter logs by activity:
   - Use the **Activity** dropdown to filter by action type (e.g., "Create policy")
   - Use the **Date range** picker to filter by time period

1. Select an audit log entry to view detailed information:
   - **Properties:** JSON payload showing before/after state (for Update actions)
   - **Actor:** UPN and IP address of the user who performed the action

   > [!NOTE]
   > Audit logs are retained for 30 days in Intune. For long-term retention, export logs to Azure Monitor or a SIEM system.

**You have successfully reviewed Intune audit logs.**

---

### Task 2: Export audit logs to CSV

1. On the **Audit logs** page, select **Export** from the top toolbar.

1. Wait for the export to complete and download the CSV file (typically 1–2 minutes for small datasets).

1. Open the CSV file in **Excel** and review the columns:
   - **Date**
   - **Activity**
   - **Initiated By**
   - **Target**
   - **Category**

**You have successfully exported audit logs for reporting.**

---

### Task 3: Understand diagnostic settings (conceptual)

Diagnostic settings route Intune logs to Azure Monitor Log Analytics for long-term retention and advanced querying.

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Diagnostics settings**.

   > [!NOTE]
   > Diagnostic settings require an Azure subscription and Log Analytics workspace. For lab purposes, review the configuration options conceptually.

1. Review the available log categories:
   - **AuditLogs:** Administrative actions in Intune

   > [!NOTE]
   > The current Intune portal exposes **AuditLogs** in this tenant. Other log categories can vary by service and tenant; don't expect **OperationalLogs** or **DeviceComplianceOrg** to appear in every portal experience.

1. Understand the configuration workflow (do not create):
   - Create a Log Analytics workspace in Azure
   - In Intune, create a diagnostic setting pointing to the workspace
   - Logs are routed to Azure Monitor for querying with KQL (Kusto Query Language)
   - Retention can be extended to 90 days, 1 year, or longer

**You now understand how diagnostic settings enable long-term log retention and advanced analytics.**

---

### Task 4: Trace the Conditional Access, compliance, and RBAC operations from earlier labs

Audit logs are how you reconstruct "who changed what, when, and why" — the bedrock of post-incident review. You'll trace the specific operations you performed across the lab series:

1. In the **Microsoft Intune admin center**, in **Tenant administration** → **Audit logs**, filter the log:
   - **Date:** In the **Date** filter, set **Start** and **End** to cover the last 7 days, then select **Apply**
   - **Activity:** In the **Activity** search box, enter `Create` and select the relevant creation activities (for example, **Create DeviceCompliancePolicy** or **Create DeviceAndAppManagementRoleAssignment**) to find policy/role creation events, then select **Apply**

1. Locate the audit log entry for **Pharmacy Helpdesk** custom role creation (from **Lab 01 Exercise 2 Task 6**). Select it and review the **Properties** → JSON payload showing the role's permission grants.

1. Locate the audit log entry for **Compliance - Windows Security Baseline** creation (from **Lab 02 Exercise 2 Task 1**). Note the **Initiated by** field shows your Global Admin account and the **Target** shows the Compliance - Windows Security Baseline policy.

1. Locate the audit log entry for the **Pharmacy Helpdesk → Lee Gu** role assignment (just created in **Exercise 3 Task 3** of this lab). Confirm the assignment payload includes the **Pharmacy** scope tag and the **dyn-Windows-Devices** group.

1. Locate the audit log entry where you **deleted** `WIN - Camera - Enabled (Pilot)` to resolve the conflict in **Lab 02 Exercise 6 Task 2**. The activity will be **Delete deviceConfiguration**. The Properties pane includes the deleted object's last-known state — useful for rollback decisions.

1. Switch to the **Microsoft Entra admin center** at **https://entra.microsoft.com**. Navigate to **Monitoring & health** → **Audit logs** (the Entra audit log, distinct from Intune's).

1. Filter the Entra audit log:
   - **Service:** Conditional Access
   - **Date:** Last 7 days

1. Locate the entry where you **switched** `CA - Require compliant device (Pharmacy pilot)` from **Report-only** to **On** (from **Lab 04 Exercise 6 Task 3**). The Properties show the policy's state change.

   > [!NOTE]
   > **Two separate audit logs.** Intune-specific actions (compliance, configuration, app, RBAC, scope tag) live in the **Intune audit log** under **Tenant administration**. Conditional Access policies, Entra role assignments, and directory operations live in the **Entra audit log** under **Identity → Monitoring & health**. When you investigate a real incident, you usually need both.

**You have successfully traced operations across both Intune and Entra audit logs.**

---

## Exercise 5: Use built-in reports

### Scenario

Intune provides built-in reports for devices, compliance, configuration, applications, and more. You'll generate and export reports for operational insights.

### Task 1: Generate a device compliance report

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Device compliance**.

1. Select the **Reports** tab, then select **Noncompliant devices and settings**.

1. Select **Generate report** (or **Run report** if previously generated).

1. Review the report data:
   - **Device name**
   - **Primary User principal name**
   - **Setting compliance state**
   - **Last check-in**
   - **Operating system**

1. Use the **Filter** option to narrow results (e.g., filter by OS = Windows).

1. Select **Export**, then select **Yes** to download the report as CSV.

**You have successfully generated and exported a device compliance report.**

---

### Task 2: Generate a device configuration report

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Device configuration**.

1. Select **Generate report**.

1. On the **Summary** tab, review the **Top 5 configuration policy status** overview:
   - **Policy name**
   - **Policy type**
   - **Successful devices**
   - **Devices with errors**
   - **Devices with conflicts**

   > [!NOTE]
   > The **Top 5 configuration policy status** table on the **Summary** tab is a read-only overview — the policy rows aren't selectable. To drill down into per-device status, navigate to **Devices** → **Manage devices** → **Configuration**, select the policy, and select **View report**.

**You have successfully generated a device configuration report.**

---

### Task 3: Review the Tenant status dashboard

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Tenant status**.

1. Review the **Tenant status** dashboard:
   - **Tenant details:** total enrolled devices, licensed users, and Intune licenses
   - **Service health and message center:** Shows active incidents or advisories affecting Intune
   - **Connector status:** Shows health of connectors (Defender for Endpoint, Microsoft Tunnel, etc.)

1. Locate **Service health** to view detailed incident information.

1. Locate **Message center** to view upcoming changes and feature rollouts.

**You have successfully reviewed the Tenant status dashboard.**

---

## Lab Summary

Congratulations! You've completed Lab 05: Automate and operate.

In this lab, you accomplished the following:

**Exercise 1: Automate with Microsoft Graph PowerShell**
- Installed the Microsoft Graph PowerShell SDK
- Registered an application for unattended automation
- Granted API permissions and created a client secret
- Authenticated with Microsoft Graph using application credentials
- Queried managed devices using Graph PowerShell
- Created and assigned a compliance policy using Graph API

**Exercise 2: Deploy proactive remediations**
- Created detection and remediation PowerShell scripts
- Uploaded a remediation script package to Intune and assigned to the pilot cohort
- Monitored remediation execution on pilot devices
- Expanded the rollout from pilot to the broader fleet

**Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end**
- Reviewed the `Pharmacy Helpdesk` role and `Pharmacy` scope tag created in **Lab 01 Exercise 2 Task 6**
- Inventoried Pharmacy-tagged objects across **Labs 02–04** (configuration, compliance, app, security baseline, ASR, BitLocker)
- Assigned the `Pharmacy Helpdesk` role to Lee Gu with the `Pharmacy` scope tag on the assignment
- Signed in as Lee Gu and verified end-to-end that only Pharmacy-tagged objects are visible — and that policy editing is blocked

**Exercise 4: Monitor audit logs and operational health**
- Reviewed Intune audit logs for administrative actions
- Exported audit logs to CSV for reporting
- Understood diagnostic settings for long-term log retention in Azure Monitor
- Traced the Conditional Access, compliance, conflict-resolution, and RBAC operations from Labs 02–04 across both the **Intune audit log** and the **Entra audit log**

**Exercise 5: Use built-in reports**
- Generated device compliance and configuration reports
- Exported report data to CSV
- Reviewed the Tenant status dashboard for service health and connector status

**Key Takeaways:**
- Microsoft Graph PowerShell enables scripted automation for bulk operations, reporting, and scope-tag-aware queries (`roleScopeTagIds` is the underlying property)
- Application permissions and client secrets allow unattended automation without user interaction
- Proactive remediations detect and fix common issues before users report problems; pilot-first rollout is the canonical pattern
- Custom RBAC roles + scope tags + group scope = the three dimensions of Intune delegated administration; the role's permissions intersect with the scope tag and the group target to produce the final visibility a delegated admin sees
- Pharmacy Helpdesk → Lee Gu is the end-to-end demonstration: a role created on day one (Lab 01) gates visibility across every policy created in Labs 02–04, with no further configuration needed in Lab 05
- Intune and Entra each have their own audit log — reach for both when investigating an incident or change
- Built-in reports and the Tenant status dashboard provide operational visibility

**Next Steps:**
In Lab 06, you'll extend Intune capabilities using the Intune Suite (Endpoint Privilege Management, Remote Help, Advanced Analytics) and explore cloud-hosted desktops (Windows 365 and Azure Virtual Desktop).

---

**END OF LAB**
