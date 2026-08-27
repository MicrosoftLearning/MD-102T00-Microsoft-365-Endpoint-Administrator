---
lab:
   title: 'Lab 04: Protect devices'
   description: 'In this lab, you integrate Microsoft Defender for Endpoint, deploy endpoint security policies, configure BitLocker encryption, deploy Microsoft Tunnel Gateway, and implement Microsoft Cloud PKI.'
   duration: 110 minutes
   level: 200
   islab: true
   primarytopics:
      - Microsoft Intune
      - Microsoft Defender for Endpoint
      - Microsoft Tunnel
      - Microsoft Cloud PKI
      - Windows
---

# Lab 04: Protect devices

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices enrolled and applications deployed, you now need to implement comprehensive security controls. You'll integrate Microsoft Defender for Endpoint for EDR capabilities, deploy endpoint security policies (antivirus, firewall, attack surface reduction), configure BitLocker encryption with Microsoft Entra key escrow, deploy Microsoft Tunnel Gateway for secure VPN access, and implement Microsoft Cloud PKI for certificate-based authentication.

By the end of this lab, you'll have:
- Enabled Microsoft Defender for Endpoint integration with Intune
- Onboarded Windows devices to Defender for Endpoint using EDR policies
- Deployed Microsoft Defender security baselines (tagged with the `Pharmacy` scope tag)
- Configured Antivirus, Firewall, and Attack Surface Reduction policies — with ASR split-assigned in **Block** mode to the pilot cohort and **Audit** mode to the broader fleet
- Created BitLocker encryption policies with Microsoft Entra recovery key escrow (tagged `Pharmacy`)
- Deployed Microsoft Tunnel Gateway on an Ubuntu server
- Created VPN profiles for Microsoft Tunnel connectivity
- Implemented Microsoft Cloud PKI with root and issuing CAs
- Created and deployed SCEP certificate profiles for device authentication
- Switched the Conditional Access policy from **Report-only** to **On** after verifying its impact

---

## Lab Duration

**Estimated Time:** 110 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- **Microsoft 365 E5** licensing (includes Defender for Endpoint P2)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Cloud PKI (Exercise 5). Microsoft Tunnel (Exercise 4) is included in Intune Plan 1 and doesn't require the Suite, but it does require the **LIN-SRV1** Ubuntu server
- Global Administrator or Intune Administrator credentials
- **SEA-DEV1** and **SEA-DEV2** (enrolled Windows 11 devices)
- **LIN-SRV1** (Ubuntu 22.04 server for Microsoft Tunnel Gateway)

> [!IMPORTANT]
> **Start this lab early.** The first-time Microsoft Defender for Endpoint tenant onboarding (Exercise 1) can take **several hours** to fully provision — device inventory, onboarding status, and security signals don't appear in the Defender portal immediately after you flip the connector on. Don't wait until Exercise 1 to check status and expect it to be fast: enable the connector and onboard your devices as soon as you start the lab, then continue with the remaining exercises while Defender finishes provisioning in the background. If you come back to verify onboarding status later and devices still show **Pending**, that's expected — give it more time before troubleshooting.

---

## Exercise 1: Integrate Microsoft Defender for Endpoint

### Scenario

Microsoft Defender for Endpoint provides EDR (Endpoint Detection and Response), advanced threat protection, and automated investigation capabilities. You'll enable the Intune-to-Defender connector and onboard Windows devices using an EDR configuration policy.

### Task 1: Enable the Microsoft Defender for Endpoint connector

The Intune ↔ Defender for Endpoint connector is a **two-portal** setup: you flip the **Microsoft Intune connection** toggle in the **Microsoft Defender portal** *first*, and only then do the **Connect Windows devices...** toggles in the **Intune** admin center become enabled. If you skip the Defender-portal step, the Intune page shows **Connection status: Unavailable** and every toggle is grayed out.

#### Part A — Establish the connection from the Microsoft Defender portal

1. In **Microsoft Edge**, open a new tab and navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Defender** portal, in the left navigation, expand **Assets** and select **Devices**.

1. On the **Device inventory** page, select **Onboard**.

1. Under **General**, select **Optional features**.

1. Locate the **Microsoft Intune connection** toggle and set it to **On**.

1. Select **Save preferences** at the bottom of the page.

   > [!NOTE]
   > Saving here is what establishes the bidirectional connector. Without this step, the Intune admin center's Defender for Endpoint page is read-only.

#### Part B — Configure the connector from the Intune admin center

1. Switch back to the Intune admin center tab (or open **https://intune.microsoft.com**).

1. In the **Microsoft Intune admin center**, select **Endpoint security**, and under the **Setup** section, select **Microsoft Defender for Endpoint**.

1. At the top of the page, select **Refresh**. **Connection status** should change from **Unavailable** to **Available** within a minute (it may take 1–2 minutes the first time).

1. On the **Endpoint security | Microsoft Defender for Endpoint** page, configure the following:

- **Endpoint Security Profile Settings:**
   - **Allow Microsoft Defender for Endpoint to enforce Endpoint Security Configurations:** On
- **Compliance policy evaluation:**
   - **Connect Windows devices version 10.0.15063 and above to Microsoft Defender for Endpoint:** On

   > [!NOTE]
   > Enabling the connector allows Intune to send device data to Defender for Endpoint and receive threat intelligence. The second setting allows Defender to enforce security configurations even on devices that aren't yet fully managed by Intune.

1. Select **Save** at the top of the page.

**You have successfully enabled the Microsoft Defender for Endpoint connector.**

---

### Task 2: Create an Endpoint Detection and Response policy

Endpoint Detection and Response policies onboard devices to Defender for Endpoint by deploying the required sensor and configuration.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint detection and response**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** Endpoint detection and response

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `EDR - Defender Onboarding`
   - **Description:** `Onboards Windows devices to Microsoft Defender for Endpoint`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Microsoft Defender for Endpoint client configuration package type:** **Auto from connector**
   - **Sample Sharing:** **All (Default)**
   - **[Deprecated] Telemetry Reporting Frequency:** **Expedite**

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, select **search by group name...** to see the list of available groups.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created an EDR policy to onboard devices to Defender for Endpoint.**

---

### Task 3: Verify device onboarding in the Microsoft Defender portal

1. In **Microsoft Edge**, open a new tab and navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com** (if not already signed in).

1. In the **Microsoft Defender portal**, expand **Assets** in the left navigation and select **Devices**.

1. Wait 10–15 minutes for SEA-DEV1 and SEA-DEV2 to onboard to Defender for Endpoint.

   > [!NOTE]
   > Device onboarding can take 10–30 minutes after the EDR policy is applied. You can force a device sync in Intune to accelerate the process.

1. After devices appear, select **SEA-DEV1** from the device list.

1. Review the device details:
   - **Risk level:** Low, Medium, High, or Secure
   - **Exposure level:** Based on security configuration score
   - **Sensor health state:** Active, Inactive, or Misconfigured
   - **Onboarding status:** Onboarded

**You have successfully verified device onboarding to Microsoft Defender for Endpoint.**

---

## Exercise 2: Deploy endpoint security policies

### Scenario

Endpoint security policies provide targeted security controls without the complexity of full configuration profiles. You'll deploy the Microsoft Defender security baseline, antivirus policies, firewall policies, and attack surface reduction rules.

### Task 1: Deploy the Microsoft Defender security baseline

Security baselines are pre-configured collections of recommended settings based on Microsoft security guidance.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Security baselines**.

1. Select **Microsoft Defender for Endpoint Security Baseline** from the list.

1. Select **+ Create policy**.

1. In the **Create a profile** pane, select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Security Baseline - Defender for Endpoint`
   - **Description:** `Microsoft-recommended security settings for Defender for Endpoint`

1. Select **Next**.

1. On the **Configuration settings** tab, review the default settings.

   > [!NOTE]
   > The baseline includes settings for:
   > - BitLocker encryption
   > - Credential Guard
   > - Application Guard
   > - Attack Surface Reduction rules
   > - Exploit protection
   > - Network protection

1. Scroll through the categories and note the pre-configured values. You can customize individual settings, but for this lab, accept the defaults.

1. Select **Next**.

1. On the **Scope tags** tab, select **+ Select scope tags**, select **Pharmacy** (created in **Lab 01 Exercise 2 Task 6**) and select **Select**. Remove the **Default** scope tag if present.

1. Select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully deployed the Microsoft Defender security baseline.**

---

### Task 2: Create an Antivirus policy

Antivirus policies configure Microsoft Defender Antivirus settings, including real-time protection, cloud protection, and scanning behavior.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Antivirus**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** Microsoft Defender Antivirus

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Antivirus - Defender Configuration`
   - **Description:** `Configures real-time protection, cloud protection, and scan settings`

1. Select **Next**.

1. On the **Configuration settings** page, expand **Defender** and configure:
   - **Allow Archive Scanning:** Allowed
   - **Allow Behavior Monitoring:** Allowed
   - **Allow Cloud Protection:** Allowed
   - **Allow Full Scan Removable Drive Scanning:** Allowed
   - **Allow Realtime Monitoring:** Allowed
   - **Allow Scanning Network Files:** Allowed
   - **Cloud Block Level:** High
   - **Cloud Extended Timeout:** 50 seconds
   - **Scan Parameter:** Quick scan
   - **Schedule Scan Day:** Every day
   - **Schedule Scan Time:** 120 (minutes after midnight, which is 2:00 AM)
   - **Submit Samples Consent:** Send all samples automatically
   - **Allow On Access Protection:** Allowed

   > [!NOTE]
   > All of these live under the single **Defender** category on this page — there's no separate "Scans" section to expand. The category has dozens of other settings (archive/CPU/network-parsing options, threat severity remediation actions, and more); leave everything not listed above at its default **Not configured**. You only need to touch the fields above for this lab.

1. Select **Next**.

1. On the **Scope tags** tab, select **Search for scope tags...**, add **Pharmacy** and select **Next**.

1. On the **Assignments** tab, search and select **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

> [!IMPORTANT]
> **Endpoint security policy precedence.** You just deployed the Defender security baseline (Task 1) AND a standalone Antivirus policy (Task 2). Both touch some of the same Defender Antivirus settings (real-time monitoring, cloud protection). Intune resolves overlapping endpoint-security settings using policy **priority** — the more recently created or higher-priority policy wins per setting, and any unresolvable conflict surfaces in **Endpoint security** → **All devices** with a **Conflict** state. In production, choose one source of truth per setting category: either let the baseline own it, or strip the setting out of the baseline and use a standalone policy.

**You have successfully created an Antivirus policy.**

---

### Task 3: Create a Firewall policy

Firewall policies configure Windows Defender Firewall rules and behavior.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Firewall**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** Windows Firewall

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Firewall - Defender Configuration`
   - **Description:** `Enables the firewall for all network profiles`

1. Select **Next**.

1. On the **Configuration settings** page, use the **Search** box to find and configure each setting below.

1. Configure **Domain Network Firewall**:
   - **Enable Domain Network Firewall:** True (Default)
   - **Disable Stealth Mode:** False (Default)
   - **Enable Log Success Connections:** Enable Logging Of Successful Connections
   - **Enable Log Dropped Packets:** Enable Logging Of Dropped Packets

1. Configure **Private Network Firewall** and use the same settings as the Domain profile:
   - **Enable Private Network Firewall:** True (Default)
   - **Disable Stealth Mode:** False (Default)
   - **Enable Log Success Connections:** Enable Logging Of Successful Connections
   - **Enable Log Dropped Packets:** Enable Logging Of Dropped Packets

1. Configure **Public Network Firewall**:
   - **Enable Public Network Firewall:** True (Default)
   - **Disable Stealth Mode:** False (Default)
   - **Default Inbound Action for Public Profile:** Block (Default)
   - **Enable Log Success Connections:** Enable Logging Of Successful Connections
   - **Enable Log Dropped Packets:** Enable Logging Of Dropped Packets

   > [!NOTE]
   > **Enable Log Success Connections** and **Enable Log Dropped Packets** return **three rows** each (one per profile) when searched — that's why each profile above lists them separately, even though the field name is identical across rows.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully created a Firewall policy.**

---

### Task 4: Create an Attack Surface Reduction (ASR) policy with split pilot/audit assignment

Attack Surface Reduction rules block behaviors commonly used by malware, such as launching executables from Office documents or running obfuscated scripts. The upper-intermediate ASR rollout pattern is to enable rules in **Block** mode on the pilot cohort while keeping them in **Audit** mode for everyone else — you get real enforcement on a small group to surface false positives early, while the rest of the fleet generates Audit logs you can use to predict broad-rollout impact. You'll do that here by creating two policies with the same rules but different modes, assigned to different groups.

#### Policy 1 — ASR Block mode for the pilot cohort

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Attack surface reduction**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** Attack Surface Reduction Rules

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `ASR - Block (Pilot)`
   - **Description:** `ASR rules in Block mode for pilot cohort — real enforcement on a small group`

1. Select **Next**.

1. On the **Configuration settings** tab, configure the following ASR rules **all in Block mode**:

   - **Block executable content from email client and webmail:** Block
   - **Block all Office applications from creating child processes:** Block
   - **Block Office applications from creating executable content:** Block
   - **Block Office applications from injecting code into other processes:** Block
   - **Block JavaScript or VBScript from launching downloaded executable content:** Block
   - **Block execution of potentially obfuscated scripts:** Block
   - **Block Win32 API calls from Office macros:** Block
   - **Block credential stealing from the Windows local security authority subsystem:** Block
   - **Block process creations originating from PSExec and WMI commands:** Block
   - **Block untrusted and unsigned processes that run from USB:** Block
   - **Block persistence through WMI event subscription:** Block

1. Select **Next**.

1. On the **Scope tags** tab, select **Search for scope tags...**, add **Pharmacy** and select **Next**.

1. On the **Assignments** tab, assign to **sg-Intune-Pilot-Users** (the pilot cohort from **Lab 01 Exercise 1**).

1. Select **Next** → **Create**.

#### Policy 2 — ASR Audit mode for the broader fleet

1. On the **Endpoint security | Attack surface reduction** page, select **+ Create Policy** again.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** Attack Surface Reduction Rules

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `ASR - Audit (Fleet)`
   - **Description:** `Same ASR rules in Audit mode for the broader fleet — generates Audit logs without enforcement`

1. Select **Next**.

1. On the **Configuration settings** tab, configure the **same ASR rules listed above**, but set each one to **Audit** mode instead of **Block** mode. (One exception: keep `Block credential stealing from lsass.exe` in **Block** mode — it's the lowest false-positive rate ASR rule and worth enforcing fleet-wide on day one.)

1. Select **Next**.

1. On the **Scope tags** tab, leave the **Default** scope tag (this is fleet-wide). Select **Next**.

1. On the **Assignments** tab, search and select **dyn-Windows-Devices**. Add **sg-Intune-Pilot-Users** (so pilot members only get the Block policy, not both) and set its **Target type** to **Exclude**.

1. Select **Next** → **Create**.

> [!NOTE]
> The split-mode pattern (Block on pilot, Audit on everyone else) is the canonical ASR rollout. Watch **Reports** → **Endpoint security** → **Attack surface reduction rules** for a week or two; when the Audit log shows the rules would have fired only on legitimate threats (no false positives in the broader fleet), flip the Audit policy to Block.

**You have successfully created split-assignment ASR policies for pilot Block and fleet Audit.**

---

## Exercise 3: Configure BitLocker encryption

### Scenario

BitLocker encrypts the entire OS drive, protecting data at rest. You'll configure a BitLocker policy that requires TPM+PIN protection and escrows recovery keys to Microsoft Entra ID.

### Task 1: Create a BitLocker policy

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Disk encryption**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows
   - **Profile:** BitLocker

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `BitLocker - Full Disk Encryption`
   - **Description:** `Requires BitLocker encryption with TPM and PIN, recovery keys escrowed to Entra ID`

1. Select **Next**.

1. On the **Configuration settings** tab, expand **BitLocker** and configure:
   - **Require Device Encryption:** Enabled
   - **Allow Warning for Other Disk Encryption:** Enabled

1. Expand **Fixed Data Drives** and configure:
   - **Enforce drive encryption type on fixed data drives:** Enable
   - **Choose how BitLocker-protected fixed drives can be recovered:** Enabled
   - **Save BitLocker recovery information to AD DS for operating system drives:** True
   - **Do not enable BitLocker until recovery information is stored in AD DS for operating system drives:** True

1. Expand **Operating System Drives** and configure:
   - **Enforce drive encryption type on fixed data drives:** Enable
   - **Require additional authentication at startup:** Enabled
   - **Configure TPM startup key:** Require startup key with TPM
   - **Compatible TPM startup key and PIN:** Require startup key and PIN with TPM
   - **Configure TPM startup:** Do not allow TPM
   - **Configure TPM startup PIN:** Do not allow startup PIN with TPM
   - **Configure minimum PIN length for startup:** Enabled
   - **Minimum characters:** 6
   - **Choose how BitLocker-protected operating system drives can be recovered:** Enabled
   - **Save BitLocker recovery information to AD DS for operating system drives:** True
   - **Configure user storage of BitLocker recovery information:** Require 48-digit recovery password

   > [!NOTE]
   > Requiring TPM+PIN provides two-factor protection: something you have (TPM chip) + something you know (PIN). Recovery keys escrowed to Entra ID allow IT admins to retrieve keys when users forget their PIN.

1. Select **Next**.

1. On the **Scope tags** tab, search and select **Pharmacy**, then select **Next**. BitLocker on Pharmacy clinical workstations is a HIPAA control — keeping the policy under the `Pharmacy` scope tag means the Pharmacy Helpdesk (assigned in **Lab 05 Exercise 3**) can see and audit it.

1. On the **Assignments** tab, search and select **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully created a BitLocker encryption policy.**

---

### Task 2: Monitor BitLocker encryption status

1. On **SEA-DEV1**, wait 10–15 minutes for the BitLocker policy to apply.

   > [!NOTE]
   > BitLocker encryption can take 1–3 hours to complete depending on drive size and system performance. For lab purposes, you'll verify the policy was applied and encryption started.

1. On **SEA-DEV1**, open **Terminal (Admin)** (right-click Start → Terminal (Admin); Windows Terminal opens a PowerShell tab by default).

1. On the **Do you want to allow this app to make changes to your device?** prompt, select **Yes**.

1. Check BitLocker status:

   ```powershell
   manage-bde -status C:
   ```

1. Review the output:
   - **Conversion Status:** Should show "Encryption in Progress" or "Fully Encrypted"
   - **Encryption Method:** XTS-AES 128 or XTS-AES 256
   - **Protection Status:** Protection On
   - **Lock Status:** Unlocked

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices** → **SEA-DEV1**.

1. Select **Recovery keys** from the left navigation.

1. Verify the BitLocker recovery key for the C: drive is escrowed to Microsoft Entra ID.

   > [!NOTE]
   > Recovery keys are stored in Entra ID and can be retrieved by Global Administrators or Helpdesk Administrators when a user forgets their BitLocker PIN.

   > [!NOTE]
   > **No BitLocker recovery key found for this device** message is expected at first. The key isn't escrowed until encryption starts (**Protection On**) *and* the device syncs afterward — with TPM+PIN this can lag 10–30 minutes.

**You have successfully monitored BitLocker encryption status and verified recovery key escrow.**

---

### Task 3: Retrieve a BitLocker recovery key

> [!NOTE]
> If no recovery key is shown yet, skip this task and return to it later. The key only appears here once BitLocker has started encrypting (**Protection On**) and the device has escrowed the key to Microsoft Entra ID — which can take some time. Continue with **Exercise 4** and revisit **Task 3** once the key populates on the **Recovery keys** blade.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices** → **SEA-DEV1**.

1. Select **Recovery keys** from the left navigation.

1. Locate the recovery key for the **C:** drive.

1. Select **Show recovery key** (if prompted, confirm with MFA or re-authenticate).

1. The recovery key is displayed in the following format:
   ```
   123456-789012-345678-901234-567890-123456-789012-345678
   ```

   > [!NOTE]
   > This key can be used to unlock the drive if the TPM fails or the user forgets their PIN. In a production environment, only authorized help desk staff should have access to recovery keys.

**You have successfully retrieved a BitLocker recovery key from Microsoft Entra ID.**

---

## Exercise 4: Deploy Microsoft Tunnel Gateway

### Scenario

Microsoft Tunnel is a VPN gateway solution that provides secure access to on-premises and cloud resources for mobile devices. You'll deploy the Tunnel Gateway on an Ubuntu server (LIN-SRV1), register it with Intune, and author the VPN profile mobile devices would consume.

> [!IMPORTANT]
> **Scope.** This exercise covers gateway deployment, Intune registration, and VPN profile authoring. The lab environment doesn't include a mobile device, so **live client VPN connectivity through the gateway is out of scope** — similar to how Lab 01 scopes out the live Autopilot OOBE. The lab is complete when the LIN-SRV1 server appears as **Online** in **Tenant administration** → **Microsoft Tunnel Gateway** → **Servers** (Task 4), and the VPN profile is authored and assigned (Task 5).
>
> Microsoft Tunnel Gateway is included with **Intune Plan 1** (no Suite required). If LIN-SRV1 isn't available in your lab environment, review the steps conceptually or skip to Exercise 5.

### Before you begin: working with the Linux terminal

Unlike the other VMs in this course, **LIN-SRV1** runs **Ubuntu Linux** with no graphical desktop. You interact with it entirely through a text **terminal** by typing commands and pressing **Enter**.

**Signing in.** When prompted, sign in with:

- **Username:** `labuser`
- **Password:** the password provided for LIN-SRV1 in the Skillable lab **Resources** panel (the same place you find credentials for the other VMs).

**Running commands as administrator (`sudo`).** Many setup steps start with `sudo` ("superuser do"), which runs that one command with administrator rights — the Linux equivalent of "Run as administrator" on Windows. The first time you use `sudo` in a session, you may be prompted for the `labuser` password again. As you type the password, **nothing appears on screen** (no dots or asterisks) — that's normal. Type it and press **Enter**.

**Common commands** you'll use to move around and inspect files:

| Command | What it does |
| --- | --- |
| `pwd` | Print the current directory ("where am I?"). |
| `ls` | List the files and folders in the current directory. |
| `ls -l` | List with details (permissions, size, date). |
| `cd foldername` | Change into a folder. |
| `cd ..` | Move up one folder level. |
| `cd ~` | Return to your home directory. |
| `cat filename` | Print the contents of a file to the screen. |
| `clear` | Clear the terminal screen. |

> [!TIP]
> If copy/paste or type-text isn't working reliably in the lab console, you can type the commands manually — they're short. Commands and file paths in Linux are **case-sensitive**, so type them exactly as shown.

### Task 1: Prepare the LIN-SRV1 server

1. Switch to **LIN-SRV1** (Ubuntu 22.04 server).

1. Sign in as **`labuser`** using the password provided for LIN-SRV1 in the Skillable **Resources** panel.

1. Verify Docker is installed:

   ```bash
   docker --version
   ```

   If Docker is not installed, install it:

   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl start docker
   ```

1. Verify internet connectivity:

   ```bash
   ping -c 4 8.8.8.8
   ```

1. Verify the server has an internal IP address and hostname:

   ```bash
   ip addr show
   hostname -f
   ```

   Note the internal IP/hostname (e.g., `192.168.1.100` or `LIN-SRV1.lab.local`). You'll reuse this endpoint value when you create the Tunnel Site (Task 2) and generate the certificate on LIN-SRV1 (Task 3). The gateway only needs **outbound** access to Microsoft Intune endpoints to register — no inbound ports, no public FQDN, and no publicly-trusted certificate are required for this lab.

**You have successfully prepared the LIN-SRV1 server for Microsoft Tunnel installation.**

---

### Task 2: Create the Tunnel Server configuration and Site in Intune (SEA-DEV1)

Before you install anything on LIN-SRV1, create the Intune objects the setup script expects. The setup script enrolls the server and asks which Site to join. If no Site exists yet, setup fails with: **Failed to get sites: No sites exist**.

Create a **Server configuration** first. The Site wizard requires one, and if the **Server configuration** dropdown is empty it means none exist yet in this tenant.

1. On **SEA-DEV1**, in the **Microsoft Intune admin center**, navigate to **Tenant administration** -> **Microsoft Tunnel Gateway**.

1. Select the **Server configurations** tab.

1. Select **Create new** and configure:
   - **Name:** `Contoso Tunnel Server Config`
   - **IP address range:** `169.254.0.0/16`
   - **Server port:** `443`
   - **DNS servers:** Required. Enter `192.168.1.1`
   - Leave other settings at default for this lab.

1. Select **Create**.

1. Select the **Sites** tab.

1. Select **Create** to create a new Tunnel site.

1. On the **Create a site** page, under the **Basics** tab, enter:
   - **Name:** `Contoso HQ Tunnel`
   - **Description:** `Microsoft Tunnel Gateway for mobile device VPN access`

1. Select **Next**.

1. On the **Settings** tab, configure:
   - **Public IP address or FQDN:** `192.168.1.100`
   - **Server configuration:** Select `Contoso Tunnel Server Config`.

   > [!NOTE]
   > In this hosted Skillable lab, LIN-SRV1 is behind provider-managed NAT/infrastructure and does not expose a learner-controlled public inbound endpoint.
   >
   > For this lab workflow, this field is used to satisfy Site configuration and certificate name matching. It does not validate real internet-reachable client ingress unless you explicitly test end-user tunnel connectivity from outside the lab network.
   >
   > Observed values from this lab run:
   > - Certificate SAN includes `DNS:lin-srv1` and `IP:192.168.1.100`.
   > - Site entry tested in the portal included `LIN-SRV1.lab.local`.
   >
   > To avoid SAN mismatch, keep the Site endpoint as `192.168.1.100` unless you regenerate the cert to include `LIN-SRV1.lab.local`.

1. Select **Next** until you reach the **Review + create** tab, and then select **Create**.

**You have successfully created the Tunnel Server configuration and Site in Intune.**

---

### Task 3: Install Microsoft Tunnel on LIN-SRV1

With the Server configuration and Site in place, install the Tunnel Gateway on the Ubuntu server. The setup script enrolls the server, joins it to the Site, and imports the TLS certificate you stage.

1. Switch to **LIN-SRV1**.

1. On **LIN-SRV1**, download the Microsoft Tunnel installation script:

   ```bash
   wget https://aka.ms/microsofttunneldownload -O mstunnel-setup
   chmod +x mstunnel-setup
   ```

1. Stage the TLS certificate files **before** you run setup. You may need to type these commands manually if copy/paste or text-to-type is not working correctly.

   For this lab, use a self-signed certificate so setup can complete in a single CLI flow:

   ```bash
   # Create required paths
   sudo mkdir -p /etc/mstunnel/certs /etc/mstunnel/private

   # Create a lab-only self-signed cert and key
   FQDN=$(hostname -f)
   IP=$(hostname -I | awk '{print $1}')
   sudo openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 365 \
      -keyout /etc/mstunnel/private/site.key \
      -out /etc/mstunnel/certs/site.crt \
      -subj "/CN=${FQDN}" \
      -addext "subjectAltName=DNS:${FQDN},IP:${IP}"

   sudo chmod 600 /etc/mstunnel/private/site.key
   sudo chmod 644 /etc/mstunnel/certs/site.crt
   sudo ls -l /etc/mstunnel/certs/site.crt /etc/mstunnel/private/site.key
   ```

   ![Screenshot of the LIN-SRV1 Linux terminal showing the openssl command generating the self-signed TLS certificate and private key for Microsoft Tunnel.](media/tunnel-cert-generation.png)

   > [!NOTE]
   > Tunnel expects one of these certificate formats:
   > - PEM chain at `/etc/mstunnel/certs/site.crt` and key at `/etc/mstunnel/private/site.key`
   > - or PFX at `/etc/mstunnel/private/site.pfx`
   >
   > The certificate SAN must match the server FQDN or IP used as the Tunnel endpoint.


1. Run the installation script:

   ```bash
   sudo ./mstunnel-setup
   ```

1. Follow the installation prompts:
   - Accept the license terms 
       - Press **Space** to scroll through the license agreement and enter **yes** at the prompt to accept.
   - When prompted for additional Admin Tasks and certificate verification, enter **yes** (the certificate files are already staged from the previous step).
     
      ![Screenshot of the LIN-SRV1 terminal displaying the Microsoft Tunnel setup Admin Tasks prompt for installing the TLS certificate.](media/tunnel-setup-admin-tasks.png)
   
   - The setup process will ask you to complete a device login. Note the **Device Code** in the terminal and switch back to SEA-DEV1 and open a browser to https://microsoft.com/devicelogin. Enter the **Device Code** you saved earlier and authenticate with the admin account.

     ![Screenshot of the LIN-SRV1 terminal showing the device code used to authenticate the Microsoft Tunnel Gateway agent at microsoft.com/devicelogin.](media/tunnel-setup-device-code.png)

1. Return to **LIN-SRV1** and wait for the installation to complete (typically 5–10 minutes).

   ![Screenshot of the LIN-SRV1 terminal showing the Microsoft Tunnel installation completing successfully with the server and agent running.](media/tunnel-setup-installation-successful.png)

1. Verify the Tunnel Gateway service is running:

   ```bash
    sudo mst-cli server status
    sudo mst-cli agent status
   ```

    The output should show the server and agent as **running** and **healthy**.

**You have successfully installed Microsoft Tunnel Gateway on LIN-SRV1.**

---

### Task 4: Verify the Tunnel Gateway server status in Intune

1. On **SEA-DEV1**, in the **Microsoft Intune admin center**, navigate to **Tenant administration** -> **Microsoft Tunnel Gateway**.

1. Select the **Health status** tab. You may need to wait 2-5 minutes for LIN-SRV1 to sync after setup completes.

   ![Screenshot of the Microsoft Tunnel Gateway Health status page in the Intune admin center showing LIN-SRV1 with a Healthy status.](media/tunnel-gateway-health-status.png)

1. Verify **LIN-SRV1** appears in the Servers list with status **Healthy**.

1. If status is **Unhealthy**, on LIN-SRV1 run:

   ```bash
   sudo mst-cli server status
   sudo mst-cli agent status
   sudo journalctl -u mstunnel_monitor -n 200 --no-pager
   sudo journalctl -t ocserv -n 200 --no-pager
   ```

> [!TIP]
> **Healthy** is the verifiable success criterion for this exercise. It confirms outbound registration worked, the install completed, and Intune is talking to your gateway — everything the gateway-deployment skill is meant to teach.

**You have successfully registered the Microsoft Tunnel Gateway in Intune.**

---

### Task 5: Create a VPN profile for Microsoft Tunnel

> [!NOTE]
> You'll author the VPN profile end-to-end and assign it to a group — the same workflow you'd use in production. In this lab environment no mobile device is enrolled to consume it, so the profile is authored and assigned but **client connection through the tunnel is out of scope** (see the scope callout at the top of Exercise 4).

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Manage Devices > Configuration**.

1. Select **+ Create** → **+ New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** iOS/iPadOS
   - **Profile type:** Templates → VPN

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `VPN - Microsoft Tunnel for iOS/iPadOS`
   - **Description:** `VPN profile for secure access via Microsoft Tunnel Gateway for iOS/iPadOS devices`

1. Select **Next**.

1. On the **Configuration settings** tab, you must choose a **Connection type** before any other fields appear.

   From the **Connection type** dropdown, scroll down past the third-party clients (Cisco, F5, Palo Alto, IKEv2, and so on) and select **Microsoft Tunnel**.

1. After you select **Microsoft Tunnel**, expand **Base VPN**. This section holds the only settings you need for the lab:
   - **Connection name:** `Contoso VPN` (this is the name users see on the device).
   - **Microsoft Tunnel site:** Select **Select a site**, then choose `Contoso HQ Tunnel` — the site you created in Task 2. Select **OK**.

1. Leave the remaining sections at their defaults — none are required for this lab:
   - **Per-app VPN:** Leave **Not configured**, and leave **Safari URLs**, **Associated Domains**, and **Excluded Domains** blank.
   - **On-Demand VPN Rules:** Don't add any rules, and leave **Block users from disabling automatic VPN** at **Not configured**.
   - **Proxy:** Leave **Use proxy server** off and the **Automatic configuration script**, **Address**, and **Port number** fields blank.
   - **Custom settings:** Leave empty.

   > [!TIP]
   > In production you'd use these optional sections to fine-tune behavior — for example, **On-Demand VPN Rules** to auto-connect for specific domains, **Per-app VPN** to scope the tunnel to chosen apps, or a **Proxy** for outbound filtering. For this lab, the two **Base VPN** values above are all you need.

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add all users**.

1. Select **Next** → **Create**.

**You have successfully created a VPN profile for Microsoft Tunnel.**

---

## Exercise 5: Implement Microsoft Cloud PKI

### Scenario

Microsoft Cloud PKI (part of the Intune Suite) provides a cloud-hosted certificate authority for issuing certificates to devices and users. You'll create a root CA, an issuing CA anchored to it, and a SCEP certificate profile for device authentication (e.g., for Wi-Fi, VPN, or S/MIME encryption). With the Suite trial active (from **Lab 01** prerequisites), this exercise is fully hands-on.

### Task 1: Create a root Certificate Authority

The root CA is the trust anchor for your Cloud PKI hierarchy. You must create at least one root CA before you can create an issuing CA.

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Cloud PKI**.

1. Select **+ Create** from the top toolbar.

   > [!NOTE]
   > **+ Create** opens the **Create certification authority** wizard directly. There's no dropdown menu choice between "Root CA" and "Issuing CA" — you pick the **CA type** on the **Configuration settings** tab inside the wizard.

1. On the **Basics** tab, enter:
   - **Name:** `Contoso Root CA`
   - **Description:** `Microsoft Cloud PKI root CA for Contoso Healthcare`

1. Select **Next** to continue to **Configuration settings**.

1. On the **Configuration settings** tab, configure:
   - **CA type:** Root CA
   - **Validity period:** **25 years** (allowed values: 5, 10, 15, 20, or 25)

1. Under **Extended Key Usages**, choose how the CA can be used. For this lab, leave **Client Auth (1.3.6.1.5.5.7.3.2)** and **Server Authentication (1.3.6.1.5.5.7.3.1)** selected (the common defaults for SCEP-issued device certificates).

   > [!IMPORTANT]
   > Root CA EKU constraints are a **superset** of the issuing CA. Any EKU you want on a downstream issuing CA must be defined here on the root first. The **Any Purpose (2.5.29.37.0)** EKU is intentionally absent — it's overly permissive and a security risk.

1. Under **Subject attributes**, enter:
   - **Common name (CN):** `Contoso Root Certificate Authority`
   - **Organization (O):** `Contoso Healthcare`
   - **Country (C):** United States of America (the) (Intune enforces a two-character limit per PKI standards)

1. Under **Encryption**, set **Key size and algorithm** to **RSA-4096 and SHA-512** (the strongest available; this is the upper bound that downstream issuing CAs and SCEP profiles can use).

1. Select **Next** to continue to **Scope tags**.

1. On the **Scope tags** tab, leave the **Default** scope tag (Cloud PKI infrastructure is typically tenant-wide). Select **Next**.

1. On the **Review + create** tab, review the summary. CA properties can't be edited after creation — if anything's wrong, select **Back** now.

1. Select **Create**.

1. Wait for the root CA to provision (typically 2–3 minutes). Select **Refresh** on the Cloud PKI list to see it appear with **Status: Active** and **Type: Root**.

**You have successfully created a cloud-hosted root Certificate Authority.**

---

### Task 2: Create an issuing Certificate Authority

Issuing CAs are subordinate to a root CA and they're what your devices actually request certificates from (via the SCEP service Cloud PKI provides automatically).

1. On the **Cloud PKI** page, select **+ Create** again.

1. On the **Basics** tab, enter:
   - **Name:** `Contoso Issuing CA`
   - **Description:** `Microsoft Cloud PKI issuing CA anchored to Contoso Root CA`

1. Select **Next**.

1. On the **Configuration settings** tab, configure:
   - **CA type:** Issuing CA
   - **Root CA source:** Intune (use a root CA you created in this tenant)
   - **Root CA:** Select **Contoso Root CA** (the root you created in Task 1)
   - **Validity period:** 10 years (allowed: 2, 4, 6, 8, or 10 — must be less than or equal to the root CA's remaining lifetime)

1. Under **Extended Key Usages**, the picker is constrained to EKUs you defined on the root in Task 1. Confirm **Client Auth** and **Server Auth** are selected.

1. Under **Subject attributes**, enter:
   - **Common name (CN):** `Contoso Issuing Certificate Authority`
   - **Organization (O):** `Contoso Healthcare`
   - **Country (C):** United States of America (the)

1. Under **Encryption**, note that **Key size and algorithm** is read-only and inherited from the root CA — it displays **RSA-4096 and SHA-512** and can't be changed on the issuing CA.

1. Select **Next** → **Scope tags** (leave Default) → **Next** → **Review + create**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Review + create** tab, select **Create**. Provisioning takes 2–3 minutes while the root CA signs the issuing CA's certificate.

**You have successfully created an issuing Certificate Authority.**

---

### Task 3: Download the root and issuing CA certificates

1. On the **Cloud PKI** page, select **Contoso Root CA** from the list.

1. Under **Properties**, select **Download certificate** and save the file as `ContosoRootCA.cer`.

1. Return to the **Cloud PKI** page and select **Contoso Issuing CA**.

1. Under **Properties**, select **Download certificate** and save the file as `ContosoIssuingCA.cer`.

   > [!NOTE]
   > These certificates will be deployed to devices as trusted roots, allowing them to trust certificates issued by the Cloud PKI infrastructure.

**You have successfully downloaded the root and issuing CA certificates.**

---

### Task 4: Create a trusted certificate profile

Trusted certificate profiles deploy root and intermediate CA certificates to devices.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Configuration**.

1. Select **+ Create** → **+ New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → Trusted certificate

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Trusted Cert - Contoso Root CA`
   - **Description:** `Deploys the Contoso Root CA certificate to the Trusted Root store`

1. Select **Next**.

1. On the **Configuration settings** tab, configure:
   - **Certificate file:** Browse and select `ContosoRootCA.cer`
   - **Destination store:** Computer certificate store - Root

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups** and then search and select **dyn-Windows-Devices**.

1. Select **Next**.

1. On the **Applicability rules** tab, select **Next**.

1. On the **Review + create** tab, select **Create**.

1. Repeat steps 1–13 to create a second trusted certificate profile for the issuing CA:
   - **Name:** `Trusted Cert - Contoso Issuing CA`
   - **Certificate file:** `ContosoIssuingCA.cer`
   - **Destination store:** Computer certificate store - Intermediate

**You have successfully created trusted certificate profiles to deploy the CA chain.**

---

### Task 5: Create a SCEP certificate profile

SCEP (Simple Certificate Enrollment Protocol) profiles allow devices to request certificates from the Cloud PKI issuing CA.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Configuration**.

1. Select **+ Create** → **+ New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → SCEP certificate

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `SCEP - Device Authentication`
   - **Description:** `Issues device authentication certificates from Cloud PKI`

1. Select **Next**.

1. On the **Configuration settings** tab, configure:
   - **Certificate type:** Device
   - **Subject name format:** Common name
   - **Subject alternative name:** DNS = `{{DeviceName}}.contoso.com`
   - **Certificate validity period:** 1 year
   - **Key storage provider (KSP):** Enroll to Trusted Platform Module (TPM) KSP if present, otherwise Software KSP
   - **Key usage:** Digital signature, Key encipherment
   - **Key size (bits):** 2048
   - **Hash algorithm:** SHA-2
   - **Root Certificate:** Select **+ Root Certificate** and then select **Trusted Cert - Contoso Root CA**
   - **Extended key usage:** Enter `Client Authentication` for **Name** and select **Client Authentication (1.3.6.1.5.5.7.3.2)** for **Predefined values**.
   - **Renewal threshold (%):** 20
   - **SCEP Server URLs:** Paste the **SCEP URI** copied from the issuing CA (**Tenant administration** → **Cloud PKI** → **Contoso Issuing CA** → **Properties** → **SCEP URI**). This field isn't auto-populated — it's required and shows a validation error until you provide it.

1. Select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups** and then search and select **dyn-Windows-Devices**.

1. On the **Applicability Rules** tab, select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a SCEP certificate profile for device authentication.**

---

### Task 6: Verify certificate enrollment on SEA-DEV1

1. On **SEA-DEV1**, wait 10–15 minutes for the SCEP profile to apply and the certificate to be issued.

1. Open **Terminal (Admin)** (Windows Terminal opens a PowerShell tab by default) and run:

   ```powershell
   Get-ChildItem -Path Cert:\LocalMachine\My |
       Where-Object { $_.Issuer -like "*Contoso Issuing*" } |
       Format-List Subject, Issuer, DnsNameList, EnhancedKeyUsageList, NotAfter
   ```

1. Verify a certificate issued by **Contoso Issuing Certificate Authority** is present with:
   - **Issuer:** CN=Contoso Issuing Certificate Authority
   - **DnsNameList:** `SEA-DEV1.contoso.com` (from the SAN; the **Subject** CN may appear as the device name or a GUID depending on the subject name format)
   - **EnhancedKeyUsageList:** Client Authentication (1.3.6.1.5.5.7.3.2)

1. Open **Microsoft Management Console** by entering `mmc.exe` in PowerShell.

1. Add the **Certificates** snap-in (File → Add/Remove Snap-in... → Certificates → Add → Computer account → Local computer (the computer this console is running on) → Finish → OK).

1. Navigate to **Certificates (Local Computer)** → **Personal** → **Certificates**.

1. Verify the device authentication certificate is present and valid.

**You have successfully verified certificate enrollment using Microsoft Cloud PKI.**

---

## Exercise 6: Monitor security posture and compliance

### Scenario

You'll use the Microsoft Defender portal and Intune admin center to monitor device security posture, compliance with policies, and threat detections.

### Task 1: Review the Microsoft Defender Secure Score

1. In **Microsoft Edge**, navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Defender portal**, expand **Exposure management** and select **Secure Score** from the left navigation.

1. Review the **Secure Score** dashboard:
   - **Overall score:** On the **Overview** tab, the percentage of achieved vs. maximum possible points
   - **Recommended actions:** On the **Recommended actions** tab, security configurations you can take to increase the score
    - **History:** On the **History** tab, the score trend chart plus a dated activity log of each point change (Date/Time, Activity, Resulting points, Category, Attributed to)
   - **Score over time:** On the **Metrics & trends** tab, the trend chart showing security posture changes
  
1. Select an improvement action (e.g., "Encrypt all BitLocker-supported drives") to view details and remediation guidance.

**You have successfully reviewed the Microsoft Defender Secure Score.**

---

### Task 2: Review threat detections and alerts

1. In the **Microsoft Defender portal**, expand **Investigation & response**, select **Incidents & alerts**, and then select **Alerts**.

1. Review the list of security alerts (if any):
   - **Severity:** High, Medium, Low, Informational
   - **Alert title:** Description of the detected threat
   - **Affected devices:** Devices where the threat was detected
   - **Status:** New, In progress, Resolved

1. Select an alert to view detailed investigation information:
   - **Alert story:** Timeline of events leading to the alert
   - **Evidence:** Files, processes, or network connections involved
   - **Recommended actions:** Steps to remediate the threat

   > [!NOTE]
   > In a new lab environment with no active threats, you may see no alerts. Review the dashboard structure to understand how alerts are presented.

**You have successfully reviewed threat detections and alerts in the Microsoft Defender portal.**

---

### Task 3: Switch the Conditional Access policy from Report-only to On

In **Lab 02 Exercise 2 Task 4** you created the Conditional Access policy `CA - Require compliant device (Pharmacy pilot)` in **Report-only** mode. In **Lab 02 Exercise 6 Task 4** you inspected its impact via Sign-in logs. The endpoint security policies you deployed in Exercises 1–3 of this lab (Defender baseline, Antivirus, Firewall, ASR, BitLocker) should now have more pilot devices passing compliance evaluation. It's time to switch the CA policy from Report-only to **On**.

> [!WARNING]
> Before you enable the policy, **verify the break-glass exclusion is still in place**. If your Global Admin account is no longer in the **Exclude** list, fix that first or you risk locking yourself out of the tenant.

1. Open a new browser tab to **https://entra.microsoft.com** and sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. Navigate to **Identity Secure Score** → **Conditional Access** → **Policies**.

1. Select `CA - Require compliant device (Pharmacy pilot)`.

1. On the **Policy details** pane, select **View or Edit** and confirm:
   - **Users or agents** include `sg-Intune-Pilot-Users`
   - **Users or agents** exclude `admin@<TenantPrefix>.onmicrosoft.com` (or whichever Global Admin you use)
   - **Target resources:** All resources (formerly "All cloud apps")
   - **Grant:** Require device to be marked as compliant

1. Before flipping the switch, run a **What If** analysis:
   - From the **Conditional Access | Policies** page, select **What If** from the top toolbar.
   - Under **Identity**, set **Select identity type** to **Users**, select **Edit user**, and choose a pilot-cohort user (e.g., Megan Bowen).
   - Under **Target resource**, set **Select target type** to **Cloud apps**, then under **Cloud apps** select **Select cloud app** and choose the app to test (e.g., Office 365 Configure).
   - For **Device platform**, select **Windows**
   - For **Client app** select **Mobile apps and desktop clients - Modern authentication**
   - Select **What If**.

1. Review the results. The bottom panel shows **Policies that would apply** and **Policies that won't apply**. Confirm `CA - Require compliant device (Pharmacy pilot)` appears under **Policies that will apply** with the grant controls **Require compliant device**.

   > [!NOTE]
   > **What If** is the production-safe rehearsal for enabling any CA policy. It runs the full evaluation engine against a simulated sign-in without affecting real users. If a non-pilot user accidentally lands under "would apply" — stop and fix the assignment scope before flipping the switch.

1. Return to the **CA - Require compliant device (Pharmacy pilot)** policy details view and scroll to **Enable policy**.

1. Change **Enable policy** from **Report-only** to **On**.

1. Select **Save**.

   > [!IMPORTANT]
   > The policy is now **enforced**. The next time a pilot-cohort user signs in to any cloud app on a non-compliant device, the sign-in will be blocked with the message "Your device is not compliant with the policies set by your IT department." The user can self-remediate by addressing the failing compliance setting (e.g., enable BitLocker, install missing security updates).

1. Switch back to **Identity Secure Score** → **Conditional Access** → **Sign-in logs**. Filter to a pilot-cohort user. Open a recent sign-in entry and confirm the **Conditional Access** tab now shows the policy with a status of **Success** or **Failure** (not **Report-only: ...**).

**You have successfully enabled the Conditional Access policy, completing the compliance → CA enforcement story that started in Lab 02.**

---

## Lab Summary

Congratulations! You've completed Lab 04: Protect devices.

In this lab, you accomplished the following:

**Exercise 1: Integrate Microsoft Defender for Endpoint**
- Enabled the Intune-to-Defender connector
- Created an EDR policy to onboard devices to Defender for Endpoint
- Verified device onboarding in the Microsoft Defender portal

**Exercise 2: Deploy endpoint security policies**
- Deployed the Microsoft Defender security baseline (tagged `Pharmacy`)
- Created Antivirus and Firewall policies (Antivirus tagged `Pharmacy`)
- Created split-assignment ASR policies: Block mode on the pilot cohort, Audit mode on the broader fleet
- Observed endpoint security policy precedence and conflict surfacing

**Exercise 3: Configure BitLocker encryption**
- Created a BitLocker policy requiring TPM+PIN protection (tagged `Pharmacy`)
- Configured recovery key escrow to Microsoft Entra ID
- Verified encryption status and retrieved recovery keys

**Exercise 4: Deploy Microsoft Tunnel Gateway**
- Installed Microsoft Tunnel Gateway on an Ubuntu server
- Registered the Tunnel Gateway in Intune
- Created a VPN profile for mobile device secure access

**Exercise 5: Implement Microsoft Cloud PKI**
- Created a root Certificate Authority and issuing CA in Cloud PKI
- Deployed trusted certificate profiles to establish the CA chain
- Created a SCEP certificate profile for device authentication
- Verified certificate enrollment on managed devices

**Exercise 6: Monitor security posture and compliance**
- Reviewed the Microsoft Defender Secure Score and improvement actions
- Reviewed threat detections and alerts in the Microsoft Defender portal
- Switched the `CA - Require compliant device (Pharmacy pilot)` policy from **Report-only** to **On** after a What If rehearsal

**Key Takeaways:**
- Microsoft Defender for Endpoint provides EDR, threat protection, and automated investigation for enrolled devices
- Endpoint security policies provide targeted controls for antivirus, firewall, and exploit mitigation; overlapping settings across baselines and standalone policies resolve via priority, with unresolvable conflicts surfaced in the portal
- Security baselines implement Microsoft-recommended settings in a single policy
- The canonical ASR rollout is **Block on pilot, Audit on fleet** — enforce on a small group while predicting broader impact via Audit logs
- BitLocker with Entra ID key escrow protects data at rest and enables IT recovery
- Microsoft Tunnel provides secure VPN access for mobile devices without traditional VPN infrastructure
- Microsoft Cloud PKI eliminates the need for on-premises PKI infrastructure while providing certificate-based authentication
- The Microsoft Defender portal consolidates security monitoring, scoring, and incident response
- Flipping a Conditional Access policy from **Report-only** to **On** is a deliberate two-step process: rehearse with **What If**, verify the break-glass exclusion, then switch

**Next Steps:**
In Lab 05, you'll automate endpoint management using Microsoft Graph PowerShell, deploy proactive remediations, configure RBAC with scope tags, and use reporting and monitoring tools.

---

**END OF LAB**
