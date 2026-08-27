---
lab:
   title: 'Lab 06: Extend capabilities'
   description: 'In this lab, you configure Endpoint Privilege Management, deploy Remote Help, review Advanced Analytics, and explore Windows 365 Cloud PC and Azure Virtual Desktop scenarios.'
   duration: 90 minutes
   level: 200
   islab: true
   primarytopics:
      - Microsoft Intune
      - Endpoint Privilege Management
      - Remote Help
      - Windows 365
      - Azure Virtual Desktop
---

# Lab 06: Extend capabilities

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. You've implemented a comprehensive Intune environment (Labs 01-05) and now want to leverage premium capabilities from the **Microsoft Intune Suite**. You'll configure Endpoint Privilege Management (EPM) to control application elevation, deploy Remote Help for secure remote assistance, review Advanced Analytics dashboards, and explore cloud-hosted desktop scenarios (Windows 365 and Azure Virtual Desktop).

By the end of this lab, you'll have:
- Enabled Endpoint Privilege Management in tenant settings
- Created Windows elevation settings and elevation rules policies
- Tested EPM elevation scenarios (automatic, user-confirmed, support-approved)
- Rolled EPM out to the pilot cohort first, then expanded to the fleet (the canonical pilot-first pattern)
- Enabled Remote Help and assigned licenses
- Deployed the Remote Help app to devices
- Initiated a Remote Help session between devices
- Demonstrated that the Pharmacy Helpdesk delegated admin (Lee Gu, from **Lab 05 Exercise 3**) can launch Remote Help on Pharmacy-scoped devices only
- Reviewed Advanced Analytics dashboards (demonstration)
- Explored Windows 365 Cloud PC provisioning (demonstration)
- Reviewed Azure Virtual Desktop session host enrollment (demonstration)

---

## Lab Duration

**Estimated Time:** 90 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Endpoint Privilege Management, Remote Help, and Advanced Analytics
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **SEA-DEV1**, **SEA-DEV2**, and **SEA-DEV3** (enrolled Windows 11 devices)

---

## Exercise 1: Configure Endpoint Privilege Management (EPM)

### Scenario

Endpoint Privilege Management allows standard users to run specific applications with elevated privileges without granting full administrator rights. With the Intune Suite trial active (from **Lab 01** prerequisites), EPM is already provisioned in your tenant. You'll verify it's available, create elevation settings and rules policies, and test different elevation scenarios.

### Task 1: Verify Endpoint Privilege Management is available

**Endpoint Privilege Management** is one of the Microsoft Intune Suite add-on capabilities. With the Suite trial activated in **Lab 01** prerequisites, EPM is already provisioned in your tenant — there is no separate tenant-wide "Enable EPM" toggle. Instead, you enable EPM on individual devices by deploying a **Windows elevation settings policy** with the **Endpoint Privilege Management** setting set to **Enabled** (you'll do that in Task 2).

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint Privilege Management**.

1. Confirm the EPM blade loads with the following tabs across the top:
   - **Overview** (insights dashboard — may show "Insufficient data" on a new tenant)
   - **Reports** (elevation report, elevation requests, file trends)
   - **Policies** (where you'll create elevation settings and elevation rules policies)
   - **Reusable settings** (shared certificate groups for use across rules)
   - **Elevation requests** (live and historical support-approved elevation requests)

   > [!NOTE]
   > If the EPM blade shows a banner indicating the capability isn't licensed, return to **Lab 01 prerequisites** and complete the Microsoft Intune Suite trial activation before continuing. EPM requires either an active trial or purchased Microsoft Intune Suite licenses.

**You have successfully verified Endpoint Privilege Management is available.**

---

### Task 2: Create an elevation settings policy

Elevation settings policies define the default elevation behavior for devices — and they're also what **enables EPM on a device** in the first place. The `Endpoint Privilege Management` setting inside this policy is what installs the EPM agent and starts evaluating elevation requests.

1. In the **Microsoft Intune admin center**, on the **Endpoint Privilege Management** page, select the **Policies** tab.

1. Select **+ Create** from the top toolbar.

1. In the **Create a profile** pane, set:
   - **Platform:** Windows
   - **Profile:** Windows elevation settings policy

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Settings - Default Behavior`
   - **Description:** `Default EPM settings for the Contoso fleet`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Endpoint Privilege Management:** Enabled (this is the toggle that actually enables EPM on the device; leaving it disabled or removing the policy disables EPM on those devices after seven days)
   - **Default elevation response:** Require user confirmation
      - **Validation:** Business justification (require the user to enter a reason)
   - **Send elevation data for reporting:** Yes
      - **Reporting scope:** Diagnostic data and managed elevations only (enables the **Elevation report** under the **Reports** tab to populate)

   > [!NOTE]
   > The four elevation responses are **Not Configured**, **Deny all requests**, **Require support approval**, and **Require user confirmation**. "Not Configured" behaves the same as "Deny all requests". Pick `Require user confirmation` for this lab so you can see the EPM prompt later in Task 6 — in production, the security-stronger choice for unknown files is `Deny all requests` paired with explicit elevation rules.

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select** → **Next** → **Create**.

**You have successfully created an elevation settings policy.**

---

### Task 3: Create an automatic elevation rule

Automatic elevation rules allow specific applications to always run elevated without user prompts.

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Elevation rules policy**. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Rules - Automatic Elevation`
   - **Description:** `Allows Registry Editor to always run elevated`

1. Select **Next**.

1. On the **Configuration settings** tab, expand **Privilege Management** and select **Add** to add a new elevation rule.

1. Select **+ Edit instance**, then in the **Rule properties** pane, configure:
   - **Rule name:** `Elevate Registry Editor`
   - **Description:** `Automatically elevates regedit.exe without user prompt`
   - **Elevation type:** Automatic
   - **File name:** `regedit.exe`
   - **File path:** `C:\Windows\regedit.exe`
   - **Signature source:** Not configured

1. On **SEA-DEV1**, open an elevated PowerShell window and run the following command to obtain the SHA256 hash for `regedit.exe`, then copy the hash value into the **File hash** field in the rule properties pane:
     ```powershell
     Get-FileHash -Path "C:\Windows\regedit.exe" -Algorithm SHA256
     ```

   > [!NOTE]
   > File-based rules target specific executables by path. You can also create rules based on file hash, publisher certificate, or product name for more precise targeting.

1. Select **Save** to add the rule.

1. On the **Scope tags** tab, select **Next**.

1. Select **Add groups** under **Included groups**, search and select `sg-Intune-Pilot-Users` (pilot-first rollout for EPM — same cohort as the blocking ESP, pilot update ring, and Block-mode ASR rules from earlier labs), then select **Next** → **Create**.

**You have successfully created an automatic elevation rule scoped to the pilot cohort.**

---

### Task 4: Create a user-confirmed elevation rule

User-confirmed elevation rules prompt the user to approve elevation (with optional business justification).

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Elevation rules policy**. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `EPM Rules - User Confirmed Elevation`
   - **Description:** `Prompts user to approve elevation for MSConfig`

1. Select **Next**.

1. On the **Configuration settings** tab, expand **Privilege Management** and select **Add** to add a new elevation rule.

1. In the **Rule properties** pane, configure:
   - **Rule name:** `Elevate MSConfig with User Confirmation`
   - **Elevation type:** User confirmed
   - **Validation:** Business justification (require the user to enter a reason)
   - **File name:** `msconfig.exe`
   - **File path:** `C:\Windows\System32\msconfig.exe`
   - **Signature source:** Not configured


1. On **SEA-DEV1**, open an elevated PowerShell window and run the following command to obtain the SHA256 hash for `msconfig.exe`, then copy the hash value into the **File hash** field in the rule properties pane:
     ```powershell
     Get-FileHash -Path "C:\Windows\System32\msconfig.exe" -Algorithm SHA256
     ```

1. Select **Save** → **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**, search and select `sg-Intune-Pilot-Users` (pilot-first rollout for EPM — same cohort as the blocking ESP, pilot update ring, and Block-mode ASR rules from earlier labs), then select **Next** → **Create**.

**You have successfully created a user-confirmed elevation rule scoped to the pilot cohort.**

---

### Task 5: Create a support-approved elevation rule

Support-approved elevation rules require a help desk agent to approve elevation requests remotely.

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Elevation rules policy**. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `EPM Rules - Support Approved Elevation`
   - **Description:** `Requires help desk approval for CMD elevation`

1. Select **Next**.

1. On the **Configuration settings** tab, expand **Privilege Management** and select **Add** to add a new elevation rule.

1. In the **Rule properties** pane, configure:
   - **Rule name:** `Elevate Command Prompt with Support Approval`
   - **Elevation type:** Support approved
   - **File name:** `cmd.exe`
   - **File path:** `C:\Windows\System32\cmd.exe`
   - **Signature source:** Not configured

1. On **SEA-DEV1**, open an elevated PowerShell window and run the following command to obtain the SHA256 hash for `cmd.exe`, then copy the hash value into the **File hash** field in the rule properties pane:
     ```powershell
     Get-FileHash -Path "C:\Windows\System32\cmd.exe" -Algorithm SHA256
     ```   

1. Select **Save** → **Next**

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**, search and select `sg-Intune-Pilot-Users` (pilot-first rollout for EPM — same cohort as the blocking ESP, pilot update ring, and Block-mode ASR rules from earlier labs), then select **Next** → **Create**.

> [!NOTE]
> **Pilot-first EPM rollout.** All three elevation policies target the pilot cohort initially. Watch the **Endpoint privilege management** → **Reports** → **Elevation summary** for a week. Confirm the automatic rule isn't being abused (legitimate registry edits only), the user-confirmed rule's business-justifications look reasonable, and the support-approved rule's request volume is manageable. Then expand each policy's assignment to `dyn-Windows-Devices` (with `sg-Intune-Pilot-Users` excluded). Same pattern as the ASR rollout in Lab 04 Exercise 2.

**You have successfully created a support-approved elevation rule scoped to the pilot cohort.**

---

### Task 6: Test EPM elevation on SEA-DEV3

1. Switch to **SEA-DEV3** (this device should be enrolled with a standard user account, e.g., Alex Wilber). 

   > [!NOTE]
   > If the user is not enrolled yet, sign in with the **Admin** account, select **Settings** → **Accounts** → **Access work or school** → **Connect** → **Join this device to Microsoft Entra ID** and sign in with **AlexW@<TenantPrefix>.OnMicrosoft.com**. Select **Join** and **Done** to complete enrollment. Then sign out and sign back in as **AlexW@<TenantPrefix>.OnMicrosoft.com**. If prompted to set up a PIN, do so.

1. Sign in as **AlexW@<TenantPrefix>.OnMicrosoft.com** (standard user, not a local administrator).

1. Force a device sync to apply the EPM policies:
   - **Settings** → **Accounts** → **Access work or school** → **Connected to Contoso** → **Info** → **Sync**

1. Wait 10–15 minutes for policies to apply.

   > [!NOTE]
   > On Windows 11, right-clicking shows the compact context menu. **Run with elevated access** (added by the EPM agent) normally appears there directly. If you don't see it, select **Show more options** (or press **Shift+F10**) to open the full menu. If it's still missing, the elevation settings policy hasn't finished applying to the device yet — sync the device and wait a few minutes before retrying.

1. Test **automatic elevation** (Registry Editor):
   - Open the **Start menu** and search for `regedit`
   - Select **Open file location**
   - Select **Registry Editor**, right click and select **Run with elevated access** to launch **Registry Editor**
   - Enter a business justification (e.g., "Testing automatic elevation") and select **Continue** to approve
   - **Expected behavior:** The app launches elevated without prompting (automatic elevation rule applied)

1. Test **user-confirmed elevation** (MSConfig):
   - Open the **Start menu** and search for `msconfig`
   - Select **Open file location**
   - Select **System Configuration**, right click and select **Run with elevated access** to launch **System Configuration**
   - **Expected behavior:** A prompt appears asking the user to confirm elevation and provide business justification
   - Enter a justification (e.g., "Troubleshooting startup issues") and select **Continue** to approve

1. Test **support-approved elevation** (Command Prompt):
   - Open the **Start menu** and search for `cmd`
   - Select **Open file location**
   - Right-click **Command Prompt** and select **Run with elevated access**
   - Enter a business justification (e.g., "Need elevated command prompt for script execution") and select **Continue**
   - **Expected behavior:** A prompt appears indicating the request is pending help desk approval.

   > [!NOTE]
   > In a production environment, a help desk agent would see the elevation request in the **Endpoint privilege management** dashboard and approve or deny it remotely.
   >
   > If Command Prompt opens elevated instead of prompting for approval, the support-approved rule hasn't reached the device yet. Confirm the **EPM Rules - Support Approved Elevation** policy shows a **Success** check-in for SEA-DEV3 (**Policies** → select the policy → **View report**), sync the device, and test again. If it still doesn't work after a few minutes, continue to the next task.

**You have successfully tested EPM elevation scenarios.**

---

### Task 7: Monitor EPM elevation reports

1. On **SEA-DEV1**, in the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint Privilege Management** → **Reports**.

1. Select **Elevation report** tile.

1. Review the report data:
   - **Total elevations:** Count of all elevation requests
   - **Automatic elevations:** Count of automatic approvals
   - **User-confirmed elevations:** Count of user-approved requests
   - **Support-approved elevations:** Count of help desk-approved requests
   - **Denied elevations:** Count of blocked requests

1. Select **Elevation details** to view individual elevation events:
   - **Device name**
   - **User name**
   - **Application name**
   - **Elevation type**
   - **Timestamp**
   - **Business justification** (if provided)

**You have successfully monitored EPM elevation reports.**

---

## Exercise 2: Deploy Remote Help

### Scenario

Remote Help provides secure, audited remote assistance for enrolled devices. IT administrators can remotely view and control devices to troubleshoot issues. You'll enable Remote Help, assign licenses, deploy the app, and initiate a remote session.

### Task 1: Enable Remote Help

1. In the **Microsoft Intune admin center**, select **Tenant administration** and select **Remote Help**.

1. On the **Remote Help** page, select the **Settings** tab.

1. Select **Configure** and configure the following settings:
   - **Enable Remote Help:** Enabled
   - **Allow Remote Help to unenrolled devices:** Not allowed
   - **Disable Chat:** No

1. Select **Save**.

**You have successfully enabled Remote Help.**

---

### Task 2: Assign Remote Help licenses

Remote Help requires Microsoft Intune Suite licensing.

1. In **Microsoft Edge**, navigate to **https://admin.cloud.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft 365 admin center**, expand **Users** and select **Active users**.

1. Select **Megan Bowen** (helper role—help desk or admin).

1. Select the **Licenses and apps** tab.

1. Verify **Microsoft Intune Suite** is assigned (or assign it if not present).

1. Repeat for **Joni Sherman** (sharer role—end user receiving help) and for **Lee Gu** (Pharmacy Helpdesk role).

   > [!NOTE]
   > Both the helper (IT admin) and sharer (end user) require Remote Help licensing.

**You have successfully assigned Remote Help licenses.**

---

### Task 3: Deploy the Remote Help app

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Select**.

   > [!NOTE]
   > Remote Help can also be deployed as a Microsoft Store app or pre-installed via OEM/image. For lab purposes, we'll deploy as a Win32 app.

1. On the **App information** page, select **Select app package file**.

1. On the **App package file** pane, select the folder icon and locate the Remote Help installer (provided by your lab environment or download from **https://aka.ms/downloadremotehelp**).

1. Upload the `.intunewin` package (if pre-packaged) or the `.msi` installer.

1. Select **OK**.

1. On the **App information** tab, enter:
   - **Name:** `Remote Help`
   - **Description:** `Secure remote assistance app for enrolled devices`
   - **Publisher:** Microsoft Corporation

1. Select **Next**.

1. On the **Program** tab, configure:
   - **Install command:** `remotehelpinstaller.exe /quiet acceptTerms=1`
   - **Uninstall command:** `remotehelpinstaller.exe /uninstall /quiet acceptTerms=1`
   - **Install behavior:** System

1. On the **Requirements** tab, configure:
   - **Check operating system architecture:** Select  **Yes. Specify the systems the app can be installed on**. Check **Install on x64-system**
   - **Minimum operating system:** Windows 10 1607

1. Select **Next**. On the **Detection rules** tab, set **Rules format** to **Manually configure detection rules**, then select **Add**.

1. In the **Detection rule** pane, configure:
   - **Rule type:** File
   - **Path:** `C:\Program Files\Remote help`
   - **File or folder:** `RemoteHelp.exe`
   - **Detection method:** File or folder exists
   - **Associated with a 32-bit app on 64-bit clients:** No

1. Select **OK** → **Next** until you reach the **Assignments** tab.

1. On the **Assignments** tab, select **+ Add group** and assign as **Required** the group **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully deployed the Remote Help app.**

---

### Task 4: Initiate a Remote Help session

> [!NOTE]
> If the **Remote Help** sign-in prompt shows **"Device must comply with your organization's compliance requirements":** on TPM-less lab VMs, the **Require encryption of data storage on device** compliance setting fails and marks the device noncompliant. Set it to **Not configured** in **both** the **Graph API - Windows Compliance Policy** and the **Compliance - Windows Security Baseline** (**Devices** → **Compliance** → **Graph API - Windows Compliance Policy** → **Properties** → **Compliance settings** → **System Security** → set **Require encryption of data storage on device** to **Not configured** → **Review + save**.), then **Sync** each device and confirm it shows **Compliant**.

1. On **SEA-DEV1** (helper device—Megan Bowen), wait for Remote Help to install.

1. After installation, launch **Remote Help** from the Start menu.

1. Sign in as **MeganB@<TenantPrefix>.OnMicrosoft.com** (helper role).

1. In the **About your privacy** prompt, select **Accept**.

1. In the Remote Help app, under **Give help**, select **Get a security code**.

1. A 6-digit help code is displayed (e.g., `123-456`).

1. Switch to **SEA-DEV2** (sharer device—Joni Sherman) and sign in as **JoniS@<TenantPrefix>.OnMicrosoft.com**.

1. Launch **Remote Help** from the Start menu.

1. Sign in as **JoniS@<TenantPrefix>.OnMicrosoft.com** (sharer role).

1. On the **About your privacy** prompt, select **Accept**.

1. In the Remote Help app, under **Get Help**, in the **Security code from assistant** box, enter the 6-digit code from SEA-DEV1, then select **Submit**.

1. Switch back to **SEA-DEV1**. The Remote Help app displays a prompt indicating Joni is ready to receive help. Select **View screen**.

1. On **SEA-DEV2**, a consent prompt appears asking Joni to approve the remote session.

1. On **SEA-DEV2**, select **Allow**. Megan can now view Joni's desktop.

   > [!NOTE]
   > By default, Remote Help provides view-only access. Megan can request full control by selecting **Request control** in the Remote Help toolbar. Joni must approve the full control request.

1. Switch back to **SEA-DEV1** and test the remote actions:
   - Megan can use chat to communicate with Joni
   - Megan can request control to interact with applications
   - Megan can end the session at any time

1. After testing, select **Leave** to disconnect.

**You have successfully initiated and tested a Remote Help session.**

---

### Task 5: Review Remote Help session logs

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Remote Help**.

   > [!NOTE]
   > The page opens on the **Monitor** tab by default. The three tabs are **Monitor** (current sessions, average session time, total sessions), **Settings** (where you enabled Remote Help in Task 1), and **Remote Help sessions** (per-session audit log).

1. Select the **Remote Help sessions** tab.

1. Review the session log columns:
   - **Provider ID** (the helper — for example, `MeganB@<TenantPrefix>.onmicrosoft.com`)
   - **Recipient ID** (the sharer — for example, `JoniS@<TenantPrefix>.onmicrosoft.com`)
   - **Recipient name**
   - **Device name**
   - **OS**
   - **Session start**
   - **Session end**

   > [!NOTE]
   > Session logs provide an audit trail for compliance and security reviews. All actions during the session are logged.

**You have successfully reviewed Remote Help session logs.**

---

### Task 6: Demonstrate Pharmacy Helpdesk Remote Help scope

The `Pharmacy Helpdesk` role assigned to **Lee Gu** in **Lab 05 Exercise 3** grants Read + remote-task permissions (including **Sync devices**, **Restart now**, **Collect diagnostics**) scoped to objects tagged **Pharmacy**. Remote Help inherits the same scope: Lee Gu can initiate a Remote Help session against Pharmacy-tagged devices, but not against devices outside her scope. This is the upper-intermediate "delegated remote-assistance" pattern.

1. Open a new **InPrivate** or **Incognito** browser window. Navigate to **https://intune.microsoft.com**.

1. Sign in as **LeeG@<TenantPrefix>.OnMicrosoft.com** (Lee Gu, the Pharmacy Helpdesk delegated admin).

1. In the Intune admin center as Lee Gu, navigate to **Devices** → **All devices**.

   > [!NOTE]
   > Lee Gu sees only devices that are in `dyn-Windows-Devices` and are tagged with the Pharmacy scope tag (per the role assignment configured in Lab 05 Exercise 3 Task 3). Depending on which devices you tagged with Pharmacy when you created them, this list may be smaller than what your Global Admin sees.

1. Select a Pharmacy-tagged device (e.g., **SEA-DEV1** tagged with **Pharmacy**).

1. In the device blade, locate the **New remote assistance session** option (toolbar or device actions menu).

1. Confirm Lee Gu can initiate the Remote Help session. The session opens in the Remote Help client — same flow as Task 4 above.

1. End the session.

1. Now try to select a device that's not Pharmacy-tagged (Lee Gu won't see one in her list, so this is a thought experiment): if such a device existed in her view, she would lack the **New remote assistance session** option because the role's scope tag intersection excludes it.

   > [!NOTE]
   > **The takeaway.** Scope tags on a custom role aren't just for the Configuration / Compliance / Apps surfaces — they apply to **remote-task operations** like Sync, Restart, and Remote Help. That's what makes scope-tag-based delegation actually safe: the Pharmacy Helpdesk physically cannot help (or accidentally disrupt) devices outside her domain.

1. Sign out of the InPrivate window.

**You have successfully demonstrated end-to-end that the Pharmacy Helpdesk delegated role, created in Lab 01 and assigned in Lab 05, scopes Remote Help operations exactly as designed. Thread A (custom RBAC + scope tag delegation) is now complete across all six labs.**

---

## Exercise 3: Use Advanced Analytics and Device Query

### Scenario

**Advanced Analytics** (part of the Intune Suite) provides ML-powered insights into device performance, anomaly detection, and resource utilization. **Device Query** uses Kusto Query Language (KQL) to run ad-hoc queries against Windows device telemetry — either against a single device (live) or across many devices. This is the upper-intermediate replacement for "please run remote desktop and check" — a delegated admin can answer real support questions without ever touching a user's device.

The Intune Suite trial (activated in **Lab 01** prerequisites) includes Advanced Analytics, so this exercise is fully hands-on.

> [!IMPORTANT]
> **Device prerequisite for Device Query.** A device must be **enrolled in Endpoint Analytics** before it shows up in Device Query results. Endpoint Analytics enrollment is enabled tenant-wide via **Reports** → **Endpoint analytics** → **Settings**. If you completed **Lab 02 Exercise 5 Task 1** (Enable Endpoint analytics), your devices are already enrolled and ready.

> [!NOTE]
> **Empty results are normal on a fresh tenant.** Until at least one Windows device has actually checked in to Endpoint Analytics, every multi-device Device Query in Task 3 will return **0 items**. The Get started → Prerequisites pane on the Device Query page repeats this: *"For a device to appear in device queries, it must be enrolled in Endpoint Analytics."* If your SEA-DEV1/SEA-DEV2 haven't checked in yet, run a single-device query against the device blade (Task 2) instead — those run live and don't depend on the Endpoint Analytics catalog.

> [!NOTE]
> **Telemetry latency.** Advanced Analytics dashboards (anomaly detection, resource performance, battery health) need approximately **24 hours of device telemetry** to populate meaningfully. Device Query, by contrast, runs against the device's **live state** and returns results within seconds. If your SEA-DEV1/SEA-DEV2 devices were enrolled less than 24 hours ago, the dashboards in Task 1 may show "Insufficient data" — Tasks 2 and 3 (Device Query) will still work.

### Task 1: Review Advanced Analytics dashboards

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Analytics** → **Endpoint analytics**.

1. Select **Start** to open the **Advanced Analytics**.

1. Review the **Anomalies** dashboard:
   - **Device anomalies:** Devices exhibiting unusual behavior (high CPU, frequent crashes, app hangs)
   - **User anomalies:** Users experiencing degraded experience scores
   - **Application anomalies:** Apps with high crash rates or slow start times

   > [!NOTE]
   > Anomaly detection uses ML to identify outliers from each device's own historical baseline (not a fleet-wide threshold). On a new lab device with limited history you may see empty panels or a status banner; that's expected.

1. Review the **Resource performance** dashboard:
   - **CPU performance:** Devices with sustained high CPU utilization
   - **Memory performance:** Devices with memory pressure (page faults, working-set pressure)
   - **Disk performance:** Devices with slow disk I/O

1. Review the **Battery health** dashboard (if mobile devices are enrolled):
   - **Battery capacity degradation:** Devices with reduced battery health vs. designed capacity
   - **Charging behavior:** Frequent charging cycles

**You have successfully reviewed the Advanced Analytics dashboards.**

---

### Task 2: Run live Device Query on a single device

Single-device Device Query runs a KQL query against one Windows device's live state. It's the canonical replacement for opening a remote control session just to check a service, a registry value, or an installed app version.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Windows** → select **SEA-DEV1**.

1. Under the **Monitor** section, select **Device query**.

1. In the query editor, enter and run the following query to list the CPU information for SEA-DEV1:

   ```kusto
   Cpu
   | project ProcessorId, Model, Architecture, CpuStatus, CoreCount, LogicalProcessorCount, Manufacturer
   ```

1. Select **Run**. Results appear in the **Results** tab within a few seconds.

   > [!NOTE]
   > Single-device Device Query has a **15 queries / minute** rate limit per admin and a **2048-character** query input limit. The result set is capped at 128 KB.

1. Replace the query with this one to check BitLocker encryption status on SEA-DEV1's drives:

   ```kusto
   EncryptableVolume
   | project Device, DriveLetter, ProtectionStatus, ConversionStatus, EncryptionMethod
   | join LogicalDrive on Device
   ```

1. Select **Run**. Confirm SEA-DEV1's OS drive shows **PROTECTED** — this verifies the BitLocker policy from **Lab 04 Exercise 3** is actively encrypting the drive (rather than just "assigned" in the Intune portal).

1. Replace the query with this one to verify the device's OS version:

   ```kusto
   OsVersion
   | project Device, OsVersion, OsBuildNumber, OsArchitecture
   ```

1. Select **Run**. Confirm SEA-DEV1 is running the Windows 11 24H2 build you pinned via the Feature update profile in **Lab 02 Exercise 4**.

**You have successfully run live Device Query against a single device.**

---

### Task 3: Run multi-device Device Query and build a security group from results

Multi-device Device Query runs one KQL query across every Windows device in your scope and returns one row per device. The killer feature: you can **create a Microsoft Entra security group directly from a query's results**, which means you can dynamically target Intune policies and Conditional Access at exactly the devices your query found.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Device query**.

   > [!NOTE]
   > This is the **multi-device** Device Query surface (Devices → Device query at the top of the **Manage devices** group is not present — it's a top-level item under **Devices**). It's distinct from the single-device Device Query you used in Task 2 (Devices → Windows → *device* → Monitor → Device query).

1. Expand the **example queries** section under **Getting started** on the left, and browse the pre-built samples. Microsoft maintains this list — it's the fastest way to learn the supported tables and operators.

1. Enter and run this query to find every Windows device that is **not** BitLocker-encrypted — the canonical "these devices need attention now" query:

   ```kusto
   EncryptableVolume
   | where ProtectionStatus != "PROTECTED"
   | join LogicalDrive on Device
   ```

1. Select **Run**. The Results tab returns one row per affected device.

1. With results on screen, select **Add all items to a group** from the top of the Results tab. In the dialog, name the new group `sg-Devices-Unencrypted` (description: *Devices identified by Device Query as not BitLocker-encrypted*). Select **Create group**.

   > [!NOTE]
   > **This is the upper-intermediate move.** Instead of building a dynamic device group based on a rough attribute (e.g., "deviceCategory eq 'Laptop'"), you can query the actual on-device state and turn the result into a real, addressable Microsoft Entra security group. Use it to target a remediation script, a stricter compliance policy, or a Conditional Access "block until compliant" enforcement.

1. Run a second query to find devices running an OS build older than your fleet target (Windows 11 24H2 — build number `26100`):

   ```kusto
   OsVersion
   | where OsBuildNumber < 26100
   | project Device, OsVersion, OsBuildNumber
   | order by OsBuildNumber asc
   ```

1. Select **Run**. This is your "hasn't taken the feature update yet" working list — useful for chasing devices that fall behind the Feature update profile you created in **Lab 02 Exercise 4**.

1. Run a third query to summarize the fleet by processor architecture (a quick "who has ARM64 devices" inventory):

   ```kusto
   Cpu
   | summarize DeviceCount = count() by Architecture
   ```

1. Select **Run**. The Results tab shows a summary row per architecture.

1. Select **Export** to save the result set as CSV — useful for handing a hardware inventory to procurement or for ticketing-system import.

   > [!NOTE]
   > Multi-device Device Query results respect **scope tags**. When Lee Gu (the **Pharmacy Helpdesk** delegated admin assigned in **Lab 05 Exercise 3**) runs these same queries, the results are automatically filtered to only the Pharmacy-tagged devices in her scope. Delegated admins can answer support questions about their own devices without ever seeing the rest of the tenant.

**You have successfully run multi-device Device Query and converted a query result into a Microsoft Entra security group.**

---

## Exercise 4: Explore Windows 365 Cloud PC provisioning

### Scenario

Windows 365 provides cloud-hosted Windows desktops (Cloud PCs) that users access via browser or Remote Desktop client. You'll review the provisioning process and understand how Cloud PCs integrate with Intune.

> [!NOTE]
> Windows 365 provisioning requires an Azure subscription and additional licensing. This exercise is a **guided demonstration** of the provisioning workflow.

### Task 1: Review Windows 365 provisioning policy (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Windows** → **Windows 365** → **Provisioning policies**.

   > [!NOTE]
   > If Windows 365 is not available in your tenant, review the following steps conceptually.

1. Understand the **Create provisioning policy** workflow:
   - **Basics:**
     - Policy name
     - Join type: Microsoft Entra join or Hybrid Microsoft Entra join
     - Network: Microsoft-hosted network or Azure network connection
   - **Image:**
     - Gallery image (e.g., Windows 11 Enterprise + Microsoft 365 Apps)
     - Custom image (uploaded to Azure Compute Gallery)
   - **Configuration:**
     - License type: Enterprise, Business, or Frontline
     - Region: Azure region for Cloud PC deployment
     - Enable single sign-on: Yes/No

1. Understand the **Assignment** workflow:
   - Assign provisioning policy to Microsoft Entra groups
   - Users in the group automatically receive a Cloud PC when policy is assigned
   - Cloud PC is provisioned in Azure (typically 15–30 minutes)

1. Understand the **User experience**:
   - User signs in to **https://windows365.microsoft.com**
   - Cloud PC appears in the user's dashboard
   - User can launch the Cloud PC via browser or Remote Desktop client
   - Cloud PC is managed by Intune (same policies as physical devices)

**You now understand how Windows 365 provisioning policies deploy cloud-hosted Windows desktops.**

---

### Task 2: Review Cloud PC management in Intune (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Understand that Cloud PCs appear in the device list with:
   - **Device name:** CloudPC-<username>
   - **Managed by:** Intune
   - **Ownership:** Corporate
   - **OS:** Windows 11 Enterprise

1. Understand that Cloud PCs receive the same Intune policies as physical devices:
   - Configuration profiles
   - Compliance policies
   - Applications
   - Security baselines

1. Understand Cloud PC-specific actions:
   - **Restart:** Restarts the Cloud PC
   - **Resize:** Changes the Cloud PC SKU (vCPU, RAM)
   - **Restore:** Restores the Cloud PC from a backup snapshot
   - **Reprovision:** Wipes the Cloud PC and re-provisions from the image

**You now understand how Cloud PCs are managed in Intune like physical devices.**

---

## Exercise 5: Explore Azure Virtual Desktop session host enrollment

### Scenario

Azure Virtual Desktop (AVD) provides multi-session Windows desktops for virtual desktop infrastructure (VDI) scenarios. You'll review how AVD session hosts can be enrolled in Intune for policy management.

> [!NOTE]
> AVD session host enrollment requires an Azure subscription and AVD deployment. This exercise is a **guided demonstration**.

### Task 1: Understand AVD session host enrollment (demonstration)

1. Understand the AVD architecture:
   - **Host pool:** Collection of identical session hosts (VMs)
   - **Session hosts:** Windows 11 or Windows 10 multi-session VMs
   - **Workspaces:** User-facing interface to access desktops and apps

1. Understand how session hosts are enrolled in Intune:
   - Session hosts are Microsoft Entra joined (or Hybrid joined)
   - Automatic MDM enrollment is enabled (same as physical devices in Lab 01)
   - Session hosts enroll in Intune during initial provisioning

1. Understand AVD-specific policy considerations:
   - **User-based policies:** Applied to the user session (e.g., OneDrive sync, app settings)
   - **Device-based policies:** Applied to the session host VM (e.g., BitLocker, firewall, antivirus)
   - **Multi-session optimizations:** Policies should account for multiple concurrent users (e.g., FSLogix profile containers)

**You now understand how AVD session hosts enroll in Intune and how policies are applied in multi-session environments.**

---

### Task 2: Review AVD session host in Intune (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Understand that AVD session hosts appear in the device list with:
   - **Device name:** AVD-SessionHost-<number>
   - **OS:** Windows 11 Enterprise multi-session or Windows 10 Enterprise multi-session
   - **Managed by:** Intune

1. Understand that AVD session hosts receive Intune policies:
   - Configuration profiles (e.g., Start menu layout, Edge policies)
   - Compliance policies (e.g., antivirus, firewall)
   - Applications (e.g., Microsoft 365 Apps, LOB apps)

1. Understand AVD-specific considerations:
   - Do not apply BitLocker to session hosts (managed disks are encrypted at rest in Azure)
   - Use FSLogix for user profile management (not OneDrive Known Folder Move)
   - Apply Windows Update policies carefully (coordinate with AVD maintenance windows)

**You now understand how AVD session hosts are managed in Intune.**

---

## Lab Summary

Congratulations! You've completed Lab 06: Extend capabilities — the final lab in the MD-102 series.

In this lab, you accomplished the following:

**Exercise 1: Configure Endpoint Privilege Management (EPM)**
- Enabled Endpoint Privilege Management in tenant settings
- Created an elevation settings policy defining default elevation behavior
- Created automatic, user-confirmed, and support-approved elevation rules — all targeted to the pilot cohort first
- Tested EPM elevation scenarios on a standard user device
- Monitored elevation reports for audit and compliance
- Established the pilot → fleet expansion plan for EPM rollout

**Exercise 2: Deploy Remote Help**
- Enabled Remote Help and assigned licenses to helpers and sharers
- Deployed the Remote Help app to managed devices
- Initiated a Remote Help session and tested view-only and full control access
- Reviewed Remote Help session logs for audit purposes
- Demonstrated that the Pharmacy Helpdesk delegated admin (Lee Gu, from **Lab 05 Exercise 3**) can launch Remote Help on Pharmacy-scoped devices only — completing **Thread A (custom RBAC + scope tag delegation)** end-to-end across all six labs

**Exercise 3: Use Advanced Analytics and Device Query**
- Reviewed Advanced Analytics dashboards for anomaly detection, resource performance, and battery health
- Ran live single-device KQL queries via Device Query (CPU info, BitLocker status verification, OS version)
- Ran multi-device KQL queries to find unencrypted devices and devices below the 24H2 feature-update target
- Built a Microsoft Entra security group (`sg-Devices-Unencrypted`) directly from a Device Query result set

**Exercise 4: Explore Windows 365 Cloud PC provisioning**
- Reviewed the Windows 365 provisioning policy workflow
- Understood how Cloud PCs are automatically provisioned and managed in Intune

**Exercise 5: Explore Azure Virtual Desktop session host enrollment**
- Understood AVD architecture and session host enrollment
- Reviewed how AVD session hosts are managed in Intune with user-based and device-based policies

**Key Takeaways:**
- Endpoint Privilege Management allows granular control of application elevation without granting full administrator rights; pilot-first rollout (same cohort as ESP, update ring, ASR) limits blast radius
- Remote Help provides secure, audited remote assistance with session logging for compliance
- Scope tags on a custom role apply to remote-task operations including Remote Help — the Pharmacy Helpdesk physically cannot initiate Remote Help on devices outside the Pharmacy scope
- Advanced Analytics surfaces ML-driven anomaly detection against each device's own historical baseline (not a fleet threshold); Device Query lets you ask live KQL questions of one device or the whole fleet without remote control
- The **"build a Microsoft Entra security group from query results"** pattern is the upper-intermediate move: query reality, then target policy at exactly what you found
- Windows 365 Cloud PCs are provisioned via Intune policies and managed like physical devices
- Azure Virtual Desktop session hosts enroll in Intune and receive policies for multi-session environments

**Course Completion:**
You have completed all 6 labs in the MD-102: Microsoft 365 Endpoint Administrator certification course. You are now prepared to:
- Deploy and manage Microsoft Intune in a cloud-pure environment
- Enroll devices using Microsoft Entra join and Windows Autopilot
- Configure device policies, compliance, and Windows Update management
- Deploy applications using multiple methods (Store, Win32, Microsoft 365 Apps, Enterprise App Catalog)
- Implement endpoint security with Microsoft Defender for Endpoint, BitLocker, and endpoint security policies
- Automate management with Microsoft Graph PowerShell
- Implement RBAC with scope tags for delegated administration
- Extend capabilities with Microsoft Intune Suite (EPM, Remote Help, Cloud PKI, Microsoft Tunnel)
- Support cloud-hosted desktops with Windows 365 and Azure Virtual Desktop

**Next Steps:**
- Review the MD-102 exam objectives and map your lab experience to the exam skills measured
- Practice additional scenarios in your own test tenant
- Explore the Microsoft Learn modules for MD-102 for additional conceptual knowledge
- Schedule your MD-102 certification exam when ready

Thank you for completing the MD-102 hands-on lab series!

---

**END OF LAB**
