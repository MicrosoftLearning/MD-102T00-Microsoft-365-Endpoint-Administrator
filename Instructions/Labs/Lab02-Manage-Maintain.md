---
lab:
  title: 'Lab 02: Manage and maintain devices'
  description: 'In this lab, you create device configuration profiles, compliance policies, and Windows Update rings, analyze Group Policy Objects for migration, and enable Endpoint analytics and proactive remediations.'
  duration: 100 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Windows
    - Windows Update for Business
---

# Lab 02: Manage and maintain devices

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices now enrolled in Intune (from Lab 01), you need to implement device configuration profiles, compliance policies, and Windows Update management. You'll also analyze existing Group Policy Objects for migration to Intune, enable Endpoint analytics for proactive monitoring, and deploy remediation scripts to maintain device health.

By the end of this lab, you'll have:
- Created configuration profiles using Settings Catalog and templates
- Applied the `Pharmacy` scope tag (from **Lab 01 Exercise 2 Task 6**) to configuration, compliance, and update policies
- Built compound assignment filters using both include and exclude modes
- Intentionally created conflicting configuration profiles and resolved the conflict with **Per-setting status**
- Configured compliance policies with grace-period actions for noncompliance
- Created a Conditional Access policy that requires compliant devices (**Report-only** mode — you switch it **On** in Lab 04)
- Analyzed Group Policy Objects for migration readiness using Group Policy analytics
- Configured update rings, a Feature update profile, and an Expedited Quality update policy
- Enabled Endpoint analytics and reviewed device performance insights
- Deployed a proactive remediation script
- Used the Troubleshooting blade to investigate device status, diagnose policy conflicts, and inspect Conditional Access impact

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **SEA-DEV1** (enrolled device, Megan Bowen signed in)
- **SEA-DEV2** (enrolled device, Joni Sherman signed in)
- Group Policy backup XML files (provided in lab assets)

> [!NOTE]
> **The Intune Devices workload has been reorganized.** All the configuration, compliance, scripts, and Group Policy analytics surfaces now live under a **Manage devices** group inside the Devices left navigation. **Windows updates** lives under **By platform > Windows**. **Assignment filters** has moved to **Tenant administration > Assignment filters**. This lab uses the current navigation paths throughout.
>
> **Tenant prerequisite for Exercise 5 — Remediations:** Proactive remediations require **Windows license verification**, which you'll enable as part of **Exercise 5 Task 2**. If your lab tenant doesn't own one of the required Windows/Microsoft 365 licenses, you can still walk through the wizard, but the script package won't execute on devices.

---

## Exercise 1: Create configuration profiles

### Scenario

Configuration profiles allow you to manage device settings at scale. You'll create profiles using the Settings Catalog (granular per-setting control) and built-in templates (pre-configured setting bundles).

### Task 1: Create a Settings Catalog profile

The Settings Catalog provides access to thousands of individual settings across Windows, macOS, iOS, and Android.

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Intune admin center**, select **Devices**, then under **Manage devices** select **Configuration**.

   > [!NOTE]
   > The page header reads **Devices | Configuration** and opens to the **Policies** tab by default. The other tabs are **Import ADMX** and **Monitor**.

1. Select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Settings catalog

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Config - Power Settings`
   - **Description:** `Manages power plan and display timeout settings for corporate devices`

1. Select **Next**.

1. On the **Configuration settings** tab, select **+ Add settings**.

1. In the settings picker, search for `power`.

1. Expand **Power** and check the following settings:
   - **Unattended Sleep Timeout Plugged In**
   - **Unattended Sleep Timeout On Battery**

1. Select **Close** to return to the configuration settings page.

1. Configure the settings:
   - **Unattended Sleep Timeout Plugged In:** `0` (0 seconds = never sleep unattended)
   - **Unattended Sleep Timeout On Battery:** `1800` (seconds = 30 minutes)

   > [!NOTE]
   > These settings are configured in **seconds**, not minutes — that's how the underlying CSP (`Policy CSP - Power`) is defined, and the Settings Catalog doesn't convert the unit for you. A value of `0` means Windows never automatically sleeps when unattended (useful for kiosk or always-on devices plugged in); a nonzero value conserves battery when unplugged.

1. Select **Next**.

1. On the **Scope tags** tab, select **+ Select scope tags**, add the **Pharmacy** scope tag (created in **Lab 01 Exercise 2 Task 6**), and select **Select**. Then select **Next**.

   > [!NOTE]
   > Applying scope tags at policy-creation time is what makes delegated administration actually work. The Pharmacy Helpdesk role you created in Lab 01 will be able to see and act on this policy (in **Lab 05 Exercise 3**) because of this tag.
   >
   > **Leave the Default scope tag checked too — don't remove it.** Unlike a role *definition's* own scope tag (Lab 01 Exercise 2 Task 6, where removing Default made sense because that role is Pharmacy-exclusive), this is a general policy assigned to every Windows device in the tenant, not a Pharmacy-only artifact. Adding Pharmacy alongside Default just gives the Pharmacy Helpdesk admin visibility into it too — it doesn't change what the policy actually applies to. This same rule applies everywhere else in the lab series you add the Pharmacy scope tag to a policy, app, or profile.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, review the settings and select **Create**.

**You have successfully created a Settings Catalog configuration profile.**

---

### Task 2: Create a Device Restrictions profile using a template

Templates provide pre-configured bundles of settings for common scenarios.

1. In the **Microsoft Intune admin center**, on the **Configuration** page, select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → **Device restrictions**

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Config - Device Restrictions`
   - **Description:** `Restricts Windows features and user capabilities on corporate devices`

1. Select **Next**.

1. On the **Configuration settings** tab, expand **General** and configure:
   - **Screen capture (mobile only):** Block
   - **Copy and paste (mobile only):** Not configured
   - **Manual unenrollment:** Block

1. Expand **Password** and configure:
   - **Password:** Require
   - **Required password type:** Alphanumeric
   - **Password complexity:** Numbers, lowercase, uppercase and special characters required
   - **Minimum password length:** 8
   - **Number of sign-in failures before wiping device:** 10

1. Expand **Microsoft Defender Antivirus** and configure:
   - **Real-time monitoring:** Enable
   - **Behavior monitoring:** Enable

1. Select **Next**.

1. On the **Scope tags** tab, select **+ Select scope tags**, add **Pharmacy**, and select **Select**. Then select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Applicability Rules** tab, select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a Device Restrictions profile.**

---

### Task 3: Create compound assignment filters (include and exclude modes)

Assignment filters refine policy targeting based on device properties without forcing you to create new groups. Upper-intermediate use of filters means combining multiple properties in one filter (**compound rule**) and using **include vs. exclude** mode on the same policy to layer in and out. You'll create two filters: one compound include filter, and one simple exclude filter that you'll re-use in Task 4.

#### Filter 1 — compound include filter (corporate Microsoft devices, no kiosks)

1. In the **Microsoft Intune admin center**, in the left navigation, select **Tenant administration**, then select **Assignment filters**.

   > [!NOTE]
   > Assignment filters used to live under **Devices**. In the current portal it's a tenant-wide setting under **Tenant administration**.

1. Select **Create** → **Managed devices**.

1. On the **Basics** tab, enter:
   - **Name:** `Filter - Microsoft corporate, no kiosks`
   - **Description:** `Compound rule: Microsoft-manufactured corporate devices that are not categorized as Kiosk`
   - **Platform:** Windows 10 and later

1. Select **Next**.

1. On the **Rules** tab, switch to the **rule syntax editor** (select **Edit**), then enter:

   ```text
   (device.manufacturer -eq "Microsoft") -and (device.deviceCategory -ne "Kiosk")
   ```

   > [!NOTE]
   > Compound filter rules use the same `-and` / `-or` / parentheses syntax as dynamic group rules. The rule-syntax editor is the only way to author compound filters — the simple property/operator/value picker is single-clause.

1. Select **OK** to save the rule.

1. Select **Next** and skip the **Scope Tags** tab.

1. On the **Review + create** tab, select **Create**.

#### Filter 2 — simple exclude filter (SEA-DEV1)

1. On the **Assignment filters** page, select **Create** → **Managed devices**.

1. On the **Basics** tab, enter:
   - **Name:** `Filter - SEA-DEV1 Exclude`
   - **Description:** `Excludes device SEA-DEV1 from policy assignments`
   - **Platform:** Windows 10 and later

1. Select **Next**.

1. On the **Rules** tab, configure:
   - **Property:** Device name
   - **Operator:** Equals
   - **Value:** `SEA-DEV1`

   > [!NOTE]
   > You're targeting SEA-DEV1 with **Equals** here — the include-vs-exclude decision happens when you **apply** the filter to a policy in Task 4 (you'll choose **Exclude filtered devices from assignment**).

1. Select **Next** and skip the **Scope Tags** tab.

1. On the **Review + create** tab, select **Create**.

> [!IMPORTANT]
> **Include vs. exclude is set at apply-time, not on the filter itself.** A filter just defines a set of devices. When you attach a filter to a policy assignment, you pick whether the policy should apply to those devices (**Include**) or skip them (**Exclude**). The same filter can be used in either mode on different policies.

**You have successfully created compound and simple assignment filters.**

---

### Task 4: Apply the assignment filter to a profile

You'll modify the Device Restrictions profile to exclude SEA-DEV1 using the filter you created in Task 3.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Manage devices** → **Configuration**.

1. Select **Config - Device Restrictions** from the list.

1. Scroll down until you see **Properties**.

1. In the **Assignments** section, select **Edit**.

1. Under the **sg-Intune-Pilot-Users** group assignment, select **Edit filter**, and then select **Exclude filtered devices in assignment**.

1. Choose **Filter - SEA-DEV1 Exclude** and select **Select**.

1. Select **Review + save** → **Save**.

   > [!NOTE]
   > The Device Restrictions profile will now apply to all devices in `sg-Intune-Pilot-Users` **except** SEA-DEV1. This is the include-vs-exclude pattern from Task 3: the filter defines "SEA-DEV1", and the apply-time mode (**Exclude**) flips its meaning. The same `Filter - SEA-DEV1 Exclude` could be used in **Include** mode on a different policy to *only* target SEA-DEV1.

**You have successfully applied an assignment filter to a configuration profile.**

---

### Task 5: Create two intentionally conflicting profiles for the pilot cohort

Real Intune environments accumulate overlapping policies as different admins author them over time. Two profiles targeting the same setting on the same group produce a **conflict** that surfaces in the **Per-setting status** view. You'll deliberately set up that situation now so you can diagnose and resolve it in **Exercise 6 Task 2**.

You'll create two Settings Catalog profiles for the pilot cohort that disagree on a single setting: **Allow camera**. (Why camera? Pharmacy clinical areas have HIPAA-driven restrictions on cameras near patient records, but the broader pilot cohort has admin assistants who need cameras for Teams meetings. Two well-meaning admins might author opposite policies for the same group.)

**Profile 1 — `WIN - Camera - Enabled (Pilot)`**

1. In the **Microsoft Intune admin center**, on the **Configuration** page, select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Settings catalog

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `WIN - Camera - Enabled (Pilot)`
   - **Description:** `Allow camera use on pilot devices (Teams meetings)`

1. Select **Next**.

1. On the **Configuration settings** tab, select **+ Add settings**.

1. In the settings picker, search for `camera`. Expand **Camera** (or **Devices > Camera**, depending on portal build) and check the **Allow Camera** setting. Close the picker.

1. Set **Allow Camera** to **Allowed**.

1. Select **Next**.

1. On the **Scope tags** tab, add **Pharmacy** and select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**, search for and select **sg-Intune-Pilot-Users**, then **Select**. Select **Next**.

1. On the **Review + create** page, select **Create**.

**Profile 2 — `WIN - Camera - Disabled (Pilot)`** (the conflicting twin)

1. On the **Configuration** page, select **Create** → **New Policy**.

1. **Platform:** Windows 10 and later. **Profile type:** Settings catalog. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `WIN - Camera - Disabled (Pilot)`
   - **Description:** `Block camera on pilot devices (Pharmacy clinical areas — HIPAA)`

1. Select **Next**.

1. On the **Configuration settings** tab, select **+ Add settings**, search for `camera`, expand **Camera** (or **Devices > Camera**, depending on portal build) and check **Allow Camera**, close the picker.

1. Set **Allow Camera** to **Not allowed**.

1. Select **Next**.

1. On the **Scope tags** tab, select **+ Select scope tags**, add **Pharmacy**, and select **Select**. Then select **Next**.

1. On the **Assignments** tab, assign to **sg-Intune-Pilot-Users** (same group). Select **Next**.

1. On the **Review + create** tab, select **Create**.

> [!IMPORTANT]
> You've intentionally created two profiles that **conflict** on the **Allow Camera** setting for the same group (`sg-Intune-Pilot-Users`). Intune does **not** silently merge or pick a winner — it surfaces the conflict in the **Per-setting status** view, and the affected setting on the device shows as **Conflict** with neither value applied. You'll diagnose and resolve this conflict in **Exercise 6 Task 2** — don't fix it now.

**You have successfully created two intentionally conflicting configuration profiles for the pilot cohort.**

---

## Exercise 2: Configure compliance policies

### Scenario

Compliance policies define security and health requirements for devices. Non-compliant devices can be marked as such in Microsoft Entra ID, triggering Conditional Access policies to block access to corporate resources.

### Task 1: Create a compliance notification message template

The **Send email to end user** noncompliance action needs a message template to send. There's no built-in **Default** template — you have to create one before you can select it in Task 2.

1. In the **Microsoft Intune admin center**, select **Devices**, then under **Manage devices** select **Compliance**.

1. Select the **Notifications** tab.

1. Select **+ Create notification**.

1. On the **Basics** tab, enter:
   - **Name:** `Default`

1. Select **Next**.

1. On the **Header and footer settings** tab, configure:
   - Leave **Show company logo**, **Show contact information**, and **Show company portal website link** at their defaults.

1. Select **Next**.

1. On the **Notification message templates** tab, select **Add** and configure:
   - **Locale:** English (United States)
   - **Subject:** `Your device needs attention`
   - **Message:** `Your device is out of compliance with Contoso's security policy. Please contact the Service Desk or take the recommended action in the Company Portal app to restore access.`
   - Toggle **Set to default locale**

1. Select **Save** and select **Next**.

1. Select **Next** and skip **Scope tags**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a compliance notification message template.**

---

### Task 2: Create a Windows compliance policy

1. In the **Microsoft Intune admin center**, select **Devices**, then under **Manage devices** select **Compliance**.

   > [!NOTE]
   > The page header reads **Devices | Compliance** and opens to the **Policies** tab by default. The other tabs are **Notifications**, **Retire noncompliant devices**, **Compliance settings**, **Scripts**, and **Monitor**.

1. Select the **Policies** tab, and then select **Create policy**.

1. In the **Create a policy** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Windows 10/11 compliance policy

1. Select **Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Compliance - Windows Security Baseline`
   - **Description:** `Requires BitLocker encryption, antivirus, firewall, and secure boot`

1. Select **Next**.

1. On the **Compliance settings** tab, expand **Device Health** and configure:
   - **BitLocker:** Require
   - **Secure Boot:** Require
   - **Code integrity:** Require

1. Expand **Device Properties** and configure:
   - **Minimum OS version:** `10.0.19045` (Windows 11 22H2 or Windows 10 21H2)

1. Expand **System Security** and configure:
   - **Require a password to unlock mobile devices:** Require
   - **Simple passwords:** Block
   - **Password type:** Alphanumeric
   - **Password Complexity:** Require digits, lowercase, uppercase, and special characters
   - **Minimum password length:** 8
   - **Require encryption of data storage on device:** Require
   - **Firewall:** Require
   - **Antivirus:** Require
   - **Antispyware:** Require
   - **Microsoft Defender Antimalware:** Require
   - **Microsoft Defender Antimalware minimum version:** Leave blank (any version)
   - **Microsoft Defender Antimalware security intelligence up-to-date:** Require
   - **Real-time protection:** Require

1. Select **Next**.

1. On the **Actions for noncompliance** tab, configure the default action:
   - **Mark device noncompliant:** 7 days

1. Select **Add** to add an additional action.

1. Configure the new action:
   - **Action:** Send email to end user
   - **Schedule (days after noncompliance):** 1
   - **Message template:** Select **Default** (or create a custom template)
   - **Additional recipients:** Leave blank

   > [!NOTE]
   > This sends an email to the device's primary user 1 day after the device becomes non-compliant, giving them time to remediate the issue.
   >
   > If no Default message template is available, navigate to the **Notifications** tab on the **Compliance** page first and select **+ Create notification** to create one before configuring this action.

1. Select **Next** and on the **Scope tags** tab, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, under **Included groups**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select** and then select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a Windows compliance policy with grace periods and notification actions.**

---

### Task 3: Monitor compliance policy results

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Monitor**, then select **Noncompliant devices**.

1. Review the **Noncompliant devices** report. It lists every device that has failed at least one compliance policy, with columns for:
   - **Device name**
   - **Primary UPN**
   - **Compliance status**
   - **Platform**
   - **OS version**
   - **Organization**
   - **Last check-in**
   - **Management agent**

   > [!NOTE]
   > This report can be delayed in showing the most recent information. In a new lab environment it may show **0 items**. Use **Refresh** to reload the data, **Add filters** to narrow the list, or **Export** to download the results.

1. Navigate to **Devices** → **All devices**.

1. Select **SEA-DEV1** from the device list.

1. Review the **Compliance** tab:
   - **Compliance status:** May show "Not evaluated," "Compliant," or "Not compliant"
   - **Last check-in:** Timestamp of last sync with Intune

   > [!NOTE]
   > Compliance evaluation can take 5–10 minutes after policy assignment. If the status shows "Not evaluated," select **Sync** from the top toolbar to force a policy refresh, then wait a few minutes and refresh the page.

1. If the device shows non-compliant, select **Device compliance** to view which settings failed.

**You have successfully monitored compliance policy results.**

---

### Task 4: Create a Conditional Access policy that requires device compliance (Report-only)

A compliance policy on its own doesn't block anything — it just marks devices as compliant or noncompliant. The teeth come from a **Conditional Access (CA)** policy that requires the **Marked as compliant** state for access to corporate resources. You'll create that CA policy now, but you'll start it in **Report-only** mode so you can observe its impact in this lab and **Lab 04 Exercise 6** before flipping it to **On**.

1. Open a new browser tab and navigate to **https://entra.microsoft.com** (Microsoft Entra admin center). Sign in as **admin@<TenantPrefix>.onmicrosoft.com** if prompted.

1. In the left navigation, under **Entra ID**, select **Conditional Access**.

1. On the left navigation, select **Policies**, then select **+ New policy**.

1. On the **New** policy page, configure:
   - **Name:** `CA - Require compliant device (Pharmacy pilot)`

1. Under **Assignments** → **Users or agents**, select **0 users or agents selected**:
   - On the **Include** tab, select **Select users and groups** → check **Users and groups** → select **sg-Intune-Pilot-Users** → **Select**.
   - On the **Exclude** tab, select **Users and groups** → select **admin@<TenantPrefix>.onmicrosoft.com** (or whichever account you signed in with) → **Select**.

   > [!WARNING]
   > **Always exclude at least one Global Administrator (break-glass account) from any Conditional Access policy that could block sign-in.** Report-only mode doesn't enforce, but this policy switches to **On** in **Lab 04 Exercise 6** — the exclusion must be in place *before* that switch, or you risk locking yourself out of the tenant.

1. Under **Assignments** → **Target resources**, select **No target resources selected**:
   - **Select what this policy applies to:** Resources (formerly "All cloud apps")
   - **Include:** All resources (formerly "All cloud apps")
   - Acknowledge the warning about including all apps.

1. Under **Assignments** → **Conditions**, select **0 conditions selected** → **Client apps** → **Not configured** → **Configure: Yes** → check both **Browser** and **Mobile apps and desktop clients** → **Done**.

1. Under **Access controls** → **Grant**, select **0 controls selected**:
   - Select **Grant access**.
   - Check **Require device to be marked as compliant**.
   - Leave **For multiple controls** at **Require all the selected controls**.
   - Select **Select**.

1. Under **Enable policy**, select **Report-only**.

   > [!NOTE]
   > **Report-only** evaluates the policy on every sign-in and logs the result (Success / Failure / Not applied / User action required) but does **not** enforce it. This is the canonical safe-rollout pattern for any CA policy that could block sign-in.

1. Select **Create**.

> [!NOTE]
> This CA policy was created in **Report-only** mode. You'll inspect its sign-in-log impact in **Exercise 6 Task 4** of this lab, and you'll switch it to **On** in **Lab 04 Exercise 6** after reviewing the report.

**You have successfully created a Conditional Access policy that requires device compliance (Report-only mode).**

---

## Exercise 3: Analyze Group Policy Objects

### Scenario

Contoso has existing Group Policy Objects (GPOs) from an on-premises Active Directory environment. You'll use Group Policy analytics to identify which GPO settings are supported in Intune and generate a migration report.

### Task 1: Import a Group Policy backup

1. On **SEA-DEV1**, download the GPO backup file from the course's GitHub lab repository into `C:\LabAssets\GPO-Backups\`.

   Open an elevated **Terminal (Admin)** window (right-click Start → Terminal (Admin); Windows Terminal opens a PowerShell tab by default) and run:

   ```powershell
   $dest = "C:\LabAssets\GPO-Backups"
   New-Item -Path $dest -ItemType Directory -Force | Out-Null
   $url = "https://raw.githubusercontent.com/MicrosoftLearning/MD-102T00-Microsoft-365-Endpoint-Administrator/master/Instructions/Labs/Assets/GPO_Desktop_Settings.xml"
   Invoke-WebRequest -Uri $url -OutFile "$dest\GPO_Desktop_Settings.xml"
   ```

   Alternatively, download it in the browser: open [Instructions/Labs/Assets/GPO_Desktop_Settings.xml](https://github.com/MicrosoftLearning/MD-102T00-Microsoft-365-Endpoint-Administrator/blob/master/Instructions/Labs/Assets/GPO_Desktop_Settings.xml) on GitHub, select **Download raw file**, and save it to `C:\LabAssets\GPO-Backups\`.

   > [!NOTE]
   > If your lab environment already provides the GPO backup file at `C:\LabAssets\GPO-Backups\`, you can skip the download and use the provided copy.

1. In the **Microsoft Intune admin center**, select **Devices**, then under **Manage devices** select **Group Policy analytics**.

   > [!NOTE]
   > Group Policy analytics is no longer flagged as **(preview)** — it's a generally available feature in the current portal.

1. Select **Import** from the top toolbar.

1. In the **GPO file upload** tab, select **Select a file**, then browse and navigate to `C:\LabAssets\GPO-Backups\`.

1. Select **GPO_Desktop_Settings.xml** and select **Open**.

1. Select **Next**.

1. On the **Scope tags** page, leave the **Default** scope tag (don't add Pharmacy here — this GPO analysis isn't part of the Pharmacy Helpdesk delegation thread used later in Lab 05). Select **Next**.

   > [!NOTE]
   > If you don't select a scope tag here, Default is applied automatically. Only admins scoped to whichever tag(s) you pick can see this imported GPO in the analytics list — leaving Default means any admin with Default scope (essentially everyone without a narrower custom role) can see it.

1. On the **Review + create** tab, select **Create**.

1. Wait for the import to complete (typically 1–2 minutes).

1. After import, the GPO appears in the list. The **MDM support** column shows how many settings are supported, and the aggregated **Group policy migration readiness** bars at the top of the page summarize **Ready for migration**, **Not supported**, and **Deprecated** counts.

**You have successfully imported a Group Policy backup into Group Policy analytics.**

---

### Task 2: Review the migration readiness report and migrate supported settings

1. On the **Group Policy analytics** page, select **GPO_Desktop_Settings** from the list.

1. The **Settings** tab opens to a table with one row per setting. Review the columns:
   - **Setting name** and **Group policy setting category**
   - **MDM support** — a green **Yes** or amber **No** icon (not a clickable drill-down; the row itself carries no extra detail beyond these columns)
   - **Value**, **Scope** (User/Device), **Min OS version**, **CSP name**, and **CSP mapping** (the OMA-URI, shown only for **Yes** rows)

   > [!NOTE]
   > There's no per-setting detail panel or "view recommended configuration" page — everything Group Policy analytics knows about a setting is already in this row. For `GPO_Desktop_Settings`, two settings show **Yes**: **Remove Run menu from Start Menu** and **Prevent changes to Taskbar and Start Menu Settings** (both map to `Policy` CSP settings). The rest show **No** — they're either not exposed to any MDM provider or fall outside the supported CSP list (Policy, PassportForWork, BitLocker, Firewall, AppLocker, Group Policy Preferences).

1. Select **Back** to return to the **Group Policy analytics** list.

1. Select the checkbox next to **GPO_Desktop_Settings**, then select **Migrate** from the toolbar.

1. On the **Settings to migrate** tab, select the **Migrate** checkbox for the two supported settings only:
   - **Remove Run menu from Start Menu**
   - **Prevent changes to Taskbar and Start Menu Settings**

   Leave the **No**-support settings unchecked — migrating them wouldn't produce a working setting anyway. Select **Next**.

1. On the **Configuration** tab, review the imported values (carried over from the GPO), then select **Next**.

1. On the **Profile info** tab, enter:
   - **Name:** `Migrated - GPO Desktop Settings`
   - **Description:** `Settings Catalog profile migrated from the on-premises GPO_Desktop_Settings GPO`

1. Select **Next**.

1. On the **Scope tags** tab, select **+ Select scope tags**, add **Pharmacy**, and select **Select**. Then select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**, search for and select **dyn-Windows-Devices**, then select **Select** and **Next**.

1. On the **Review + deploy** page, review the settings and select **Deploy**.

   > [!NOTE]
   > Group Policy analytics helps you plan GPO-to-Intune migrations by identifying which settings can be directly migrated vs. which require alternative approaches (custom scripts, third-party tools, or re-architecting). The **Migrate** feature is best-effort — some settings translate to a similar-but-not-identical Settings Catalog equivalent, and AppLocker/Firewall GPO settings disable **Migrate** entirely since those are configured through Endpoint Security instead.

**You have successfully reviewed a Group Policy migration readiness report and migrated the supported settings to a new Settings Catalog profile.**

---

### Task 3: Export the analysis results

1. On the **Group Policy analytics** list page, select the **GPO_Desktop_Settings** row, then select **Export** from the top toolbar.

1. The download starts immediately as a CSV file. Save it to `C:\LabAssets\GPO-Analysis-Results.csv`.

1. Open the CSV file in **Excel** or **Notepad** to review the exported data.

   The CSV contains:
   - Setting name
   - Setting category
   - Configured value
   - Migration readiness status
   - Intune equivalent (if available)

**You have successfully exported Group Policy analysis results.**

---

## Exercise 4: Configure Windows Update management

### Scenario

You'll use Windows Update for Business policies (Update rings) to control when devices receive feature and quality updates. You'll create multiple rings for phased rollouts (pilot, standard, and conservative).

### Task 1: Create a pilot update ring

1. In the **Microsoft Intune admin center**, select **Devices**, under **By platform** select **Windows**, then on the Windows blade select **Windows updates**.

   > [!NOTE]
   > The page header reads **Devices | Windows updates**. The tabs are **Releases**, **Update rings**, **Feature updates**, **Quality updates**, **Driver updates**, and **Monitor**. The page opens on **Releases** — you'll switch tabs in the next step.
   >
   > The page may also display two banners that are safe to ignore for the lab:
   >
   > - **Hotpatch Enablement** — eligible devices auto-receive Hotpatch quality updates. Leave the **Opt out** button alone.
   > - **Windows 10 reached end of support on October 14, 2025** — informational; the lab still references Windows 10.

1. Select the **Update rings** tab.

1. Select **+ Create profile**.

1. On the **Basics** tab, enter:
   - **Name:** `Update Ring - Pilot`
   - **Description:** `Pilot ring for early adopters—receives updates immediately`

1. Select **Next**.

1. On the **Update ring settings** tab, configure:
   - **Microsoft product updates:** Allow
   - **Windows drivers:** Allow
   - **Quality update deferral period (days):** 0
   - **Feature update deferral period (days):** 0
   - **Set feature update uninstall period (2–60 days):** 30

1. Under **User experience settings**:
   - **Automatic update behavior:** Auto install and restart at maintenance time
   - **Active hours start:** 8 AM
   - **Active hours end:** 5 PM
   - **Option to pause updates:** Disable
   - **Option to check for Windows updates:** Enable

1. Select **Next**.

1. On the **Scope tags** tab, add **Pharmacy** and select **Next**.

   > [!NOTE]
   > Tagging the pilot ring with `Pharmacy` keeps it visible to the Pharmacy Helpdesk (who pilots clinical updates first) when you assign the role in **Lab 05 Exercise 3**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a pilot update ring.**

---

### Task 2: Create a standard update ring

1. On the **Update rings** tab, select **+ Create profile**.

1. On the **Basics** page, enter:
   - **Name:** `Update Ring - Standard`
   - **Description:** `Standard ring for general users—defers updates by 7 days`

1. Select **Next**.

1. On the **Update ring settings** tab, configure:
   - **Quality update deferral period (days):** 7
   - **Feature update deferral period (days):** 14
   - **Automatic update behavior:** Auto install and restart at maintenance time
   - **Active hours start:** 8 AM
   - **Active hours end:** 5 PM
   - **Option to pause updates:** Enable (allows users to pause updates for up to 7 days)

1. Select **Next**.

1. On the **Scope tags** tab, select  **Next**.

1. On the **Assignments** tab, under **Included groups**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Under **Excluded groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users** (to exclude pilot users who already have the Pilot ring assigned).

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a standard update ring with deferrals.**

---

### Task 3: Monitor Windows Update deployment status

The pilot cohort (`sg-Intune-Pilot-Users`, created in **Lab 01 Exercise 1**) is the same group that received the blocking ESP in **Lab 01 Exercise 4** and the pilot configuration profile in this lab's Exercise 1. That single cohort threads through every rollout in this lab series — update rings here, ASR rules in Lab 04, remediation rollout in Lab 05, EPM in Lab 06. Watching one consistent pilot cohort across rings is what makes phased rollouts work in production.

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Windows updates**.

   The page header reads **Reports | Windows updates** and opens to the **Summary** tab, which shows two aggregated reports: **Windows Feature updates** and **Windows Expedited Quality updates**. A second **Reports** tab on the same page lists the detailed drill-in reports.

1. On the **Summary** tab, in the **Windows Feature updates** section, select **Generate report**.

1. Review the report data:
   - **Policy**
   - **Versions**
   - **In progress**
   - **Success**
   - **Error**
   - **Rollback initiated or completed**
   - **Cancelled**
   - **On hold**

1. Navigate to **Devices** → **Windows** → Select **Windows updates**.

1. Review the available Windows Update reports and policies, including **Update rings** and **Feature updates**.

1. Return to **Devices** > **All devices** and select **SEA-DEV1**.

1. On the **Overview** page, review the device's Last check-in time and compliance status.

**You have successfully monitored Windows Update deployment status.**

---

### Task 4: Create a Feature update profile

Update rings control *when* updates install. **Feature update profiles** control *which version* of Windows devices are pinned to — a separate axis. You'll create a Feature update profile that pins the broader fleet to Windows 11 24H2 while the pilot cohort runs ahead via the Pilot update ring.

1. In the **Microsoft Intune admin center**, in **Devices** → **Windows updates**, select the **Feature updates** tab.

1. Select **+ Create > Create feature update policy**.

1. On the **Deployment settings** tab, configure:
   - **Name:** `Feature Update - Win11 25H2`
   - **Description:** `Pin Contoso fleet to Windows 11 25H2`
   - **Feature update to deploy:** Windows 11, version 25H2
   - Check **Make available to users as a required update**

   > [!NOTE]
   > Use the **Gradual rollout** option in production to release the feature update to subsets of the fleet on a schedule. For this lab, immediate availability keeps the flow simple.

1. Select **Next**.

1. On the **Scope tags** tab, leave the **Default** scope tag (this profile is tenant-wide). Select **Next**.

1. On the **Assignments** tab, assign to **dyn-Windows-Devices**. Under **Exclude groups**, add **sg-Intune-Pilot-Users** (the pilot cohort runs ahead via the Pilot update ring, so excluding them here prevents the Feature update profile from holding them back).

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a Windows feature update policy.**

---

### Task 5: Create an Expedited Quality update policy

**Expedited Quality updates** push out-of-band security patches faster than the normal deferral window. They're the right answer for an active zero-day. You'll create a policy that installs the latest critical security patch within 2 days, overriding any deferral the regular Update ring would apply.

1. In **Devices** → **Windows updates**, select the **Quality updates** tab.

1. Select **+ Create > Expedite policy**.

1. On the **Settings** tab, configure:
   - **Name:** `Quality Update - Expedited critical patches`
   - **Description:** `Push out-of-band security patches within 2 days, overriding ring deferrals`
   - **Select the quality update you would like to Expedite** - choose the latest update available.
   - **If a reboot is required, select the number of days before it's enforced:** 2 days

1. Select **Next**.

1. On the **Scope tags** tab, leave **Default**. Select **Next**.

1. On the **Assignments** tab, assign to **dyn-Windows-Devices** (no exclusions — expedited security updates apply to everyone, including pilot).

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

   > [!NOTE]
   > Update rings + Feature update profiles + Expedited Quality update policies are the three layers of Windows Update for Business in Intune. Rings control timing for routine quality updates; Feature update profiles control which Windows version is offered; Expedited Quality update policies override timing for security-critical patches.

**You have successfully created an Expedited Quality update policy.**

---

## Exercise 5: Enable Endpoint analytics and proactive remediations

### Scenario

Endpoint analytics provides insights into device performance, startup times, and user experience. Proactive remediations automatically detect and fix common issues before users report problems.

### Task 1: Enable Endpoint analytics

1. In the **Microsoft Intune admin center**, select **Reports**, expand the **Analytics** group, and select **Endpoint analytics**.

1. The first time you visit Endpoint analytics in a tenant, you land on the **Endpoint analytics | Introduction** page. Leave **Collect device data from** set to **All cloud-managed devices** and select **Start** to enable data collection.

   > [!NOTE]
   > If a previous admin has already started data collection, the **Start** button won't appear and you'll land on **Overview** instead. Skip to the next step.

1. Select **Settings** in the left navigation.

1. Review the **Intune data collection policy** section.

   > [!NOTE]
   > Endpoint analytics requires devices to send diagnostic data to Microsoft. This is automatically enabled for Intune-enrolled devices.

1. Return to the **Endpoint analytics | Overview** page.

   > [!NOTE]
   > Endpoint analytics requires 24–48 hours of device telemetry before displaying meaningful insights. In a new lab environment, the dashboard will show limited data. You can still review the dashboard structure and understand the metrics tracked.

1. In the left navigation, expand the **Reports** group and review the available reports:
   - **Startup performance:** Boot times and logon durations
   - **Application reliability:** App crashes and hangs
   - **Work from anywhere:** Cloud connectivity and recommended actions
   - **Resource performance:** CPU and memory utilization
   - **Battery health:** Battery condition and runtime

**You have successfully enabled Endpoint analytics.**

---

### Task 2: Enable Windows license verification

Proactive remediations require Windows license verification to be enabled at the tenant level before you can create or run a script package. You'll enable it now, before building the remediation in Task 3.

1. In the **Microsoft Intune admin center**, select **Tenant administration**, then select **Connectors and tokens**.

1. Select **Windows data**.

1. Under **Windows license verification**, turn on **I confirm that my tenant owns one of these licenses**.

   > [!NOTE]
   > This requires being a **Global Administrator** or **Intune Service Administrator**. It confirms your tenant holds one of: Windows 10/later Enterprise E3/E5 (or Microsoft 365 F3/E3/E5), Windows 10/later Education A3/A5 (or Microsoft 365 A3/A5), or Windows Virtual Desktop Access E3/E5 — it isn't tied to the Intune Suite or a Remediations add-on. In a lab tenant without one of these licenses, you can still walk through the remediation wizard in Task 3, but the script package won't execute on devices.

1. Select **Save** if you made any changes.

**You have successfully enabled Windows license verification.**

---

### Task 3: Create a proactive remediation script package

Proactive remediations run PowerShell scripts on devices to detect and fix issues automatically.

1. In the **Microsoft Intune admin center**, select **Devices**, then under **Manage devices** select **Scripts and remediations**.

1. Select the **Remediations** tab (the page opens on this tab by default).

1. Select **+ Create**.

1. On the **Basics** tab, enter:
   - **Name:** `Remediation - Clear Temp Files`
   - **Description:** `Detects and clears temporary files older than 30 days`

1. Select **Next**.

1. On the **Settings** page, configure:
   - **Detection script file:** Select **Select a file**, then browse and navigate to `C:\LabAssets\Remediations\Detect-TempFiles.ps1` (provided in lab assets).

     > [!NOTE]
     > If the script is not present, you can create it inline following the example below:
     
     Example detection script:
     ```powershell
     # Create the folder if it doesn't exist
     New-Item -Path "C:\LabAssets\Remediations" -ItemType Directory -Force

     # Detection script
     @'
     $tempPath = "$env:TEMP"
     $oldFiles = Get-ChildItem -Path $tempPath -Recurse -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) }
     if ($oldFiles.Count -gt 0) {
         Write-Output "Found $($oldFiles.Count) old temp files"
         exit 1  # Issue detected
     } else {
         Write-Output "No old temp files found"
         exit 0  # Compliant
     }
     '@ | Set-Content -Path "C:\LabAssets\Remediations\Detect-TempFiles.ps1" -Encoding UTF8
     ```

    The closing `'@` must begin in column one. Do not indent the here-string terminator.

   - **Remediation script file:** Select **Select a file**, then browse and navigate to `C:\LabAssets\Remediations\Remediate-TempFiles.ps1`.

     Example remediation script:
     ```powershell
     # Remediation script
     @'
     $tempPath = "$env:TEMP"
     try {
         Get-ChildItem -Path $tempPath -Recurse -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item -Force
         Write-Output "Cleared old temp files"
         exit 0  # Success
     } catch {
         Write-Error "Failed to clear temp files: $_"
         exit 1  # Failure
     }
     '@ | Set-Content -Path "C:\LabAssets\Remediations\Remediate-TempFiles.ps1" -Encoding UTF8
     ```

   - **Run this script using the logged-on credentials:** No (run as SYSTEM)
   - **Enforce script signature check:** No
   - **Run script in 64-bit PowerShell:** Yes

1. Select **Next**, add the **Pharmacy** scope tag and select **Next**.

1. On the **Assignments** tab, under **Included groups**, select **+ Select groups to include**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created a proactive remediation script package.**

---

### Task 4: Monitor remediation execution

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Temp Files** from the list.

1. Select the **Device status** tab.

1. Review the device execution results:
   - **Detection status:** Shows whether the issue was detected
   - **Remediation status:** Shows whether the remediation succeeded or failed
   - **Last check-in:** Timestamp of last script execution

   > [!NOTE]
   > Proactive remediations run on a schedule (default: once per day). After initial policy deployment, wait 1–2 hours for the first execution, then check the results.

**You have successfully monitored proactive remediation execution.**

---

## Exercise 6: Use the Troubleshooting blade

### Scenario

The Troubleshooting blade provides a consolidated view of a user's devices, policies, app installations, and enrollment status. You'll use it to investigate device compliance and policy assignment.

### Task 1: Investigate a user's device status

1. In the **Microsoft Intune admin center**, select **Troubleshooting + support** and select **Troubleshoot**.

1. In the **User** field (placeholder text "Search by display name or email"), search for and select **Megan Bowen**.

1. After selecting the user, the page shows a row of tabs, not scrollable sections: **Summary**, **Devices**, **Groups**, **Policy**, **Applications**, **App protection policy**, **Updates**, and more under the **...** overflow menu.

1. Select the **Devices** tab.

1. Verify a pilot-cohort device (**SEA-DEV1** or **SEA-DEV2**) is listed for Megan Bowen.

1. Select that device from the list to open its device blade.

1. Review:
   - **Enrolled by**
   - **Last check-in time**
   - **Compliance**
   - **Primary user**
   - **Management name**

**You have successfully investigated a user's device status.**

---

### Task 2: Diagnose and resolve a policy conflict using Per-setting status

In **Exercise 1 Task 5** you intentionally created two configuration profiles — `WIN - Camera - Enabled (Pilot)` and `WIN - Camera - Disabled (Pilot)` — that conflict on the **Allow Camera** setting for the `sg-Intune-Pilot-Users` group. Now you'll find that conflict in the portal and resolve it.

> [!IMPORTANT]
> **Device prerequisite.** The **Conflict** state only appears after a Windows device has actually checked in with the conflicting policies applied. A pilot-cohort device (**SEA-DEV1** or **SEA-DEV2**) must be online and have synced at least once with the two camera profiles assigned. If you don't see **Conflict** in the steps below — only **Pending** or **Not evaluated** — go to **Devices** → select the device → **Sync** and wait 5–10 minutes.

1. You should still be on the device blade you opened at the end of **Task 1**. If not, navigate to **Devices** → **All devices** and reselect that same pilot-cohort device (**SEA-DEV1** or **SEA-DEV2**).

1. In the device blade's left navigation, under **Monitor**, select **Device configuration**.

1. Review the **State** column. This report lists every policy assigned to the device (**Policy**, **Logged in user**, **Policy type**, **State**) with a real per-policy status — this is a cleaner, more direct view than the Troubleshoot blade's **Policy** tab, which doesn't show status at all.

1. Find `WIN - Camera - Enabled (Pilot)` and `WIN - Camera - Disabled (Pilot)`. Both should show **State: Conflict**.

   > [!NOTE]
   > You may also see **Conflict** or **Error** on other unrelated policies in this list (for example, if two update rings both target this device, or an earlier profile has a genuine misconfiguration) — that's expected noise from everything else this lab series has deployed. Focus only on the two camera profiles for this task.

1. Select `WIN - Camera - Disabled (Pilot)` to open the **Policy Settings** page.

   > [!NOTE]
   > The **Policy Settings** page lists every individual setting in the profile with its resolution state in a table of **Name**, **Status**, and **Error code** columns (status values include **Success**, **Pending**, **Error**, **Conflict**, and **Not applicable**). A **Conflict** status means two or more policies are trying to set the same setting to different values — Intune cannot resolve it, so it applies neither, and the device retains its existing local value.

1. Find the **Allow Camera** row and confirm the **Status** column shows **Conflict**.

1. Resolve the conflict. Pharmacy clinical regulations win at Contoso — cameras off in clinical areas — so you'll keep the **Disabled** profile and delete the **Enabled** one:
   - Navigate back to **Devices** → **Manage devices** → **Configuration**.
   - Select **WIN - Camera - Enabled (Pilot)**.
   - From the toolbar, select **Delete**, then select **OK** to confirm.

1. Trigger a device sync (**Devices** → **All devices** → select the same device → **Sync**) and wait 2–5 minutes for the device to re-evaluate.

1. Return to the device's **Monitor** → **Device configuration** report and confirm `WIN - Camera - Disabled (Pilot)` now shows **State: Succeeded** (no longer **Conflict**), with the **Disabled** value applied.

   > [!NOTE]
   > Alternative resolutions you could have used in production: (a) change one profile's assignment so the two no longer overlap on the same group; (b) move the conflicting setting out of one profile entirely; (c) use **Settings catalog precedence** by ordering policies (where supported). Deleting the loser is the simplest — but on a real fleet, audit who created each conflicting profile and why before deleting.

**You have successfully diagnosed and resolved a real policy conflict using Per-setting status.**

---

### Task 3: Force a device sync from the Troubleshooting blade

1. On the **Troubleshooting + support | Troubleshoot** page (with Megan Bowen selected), in the **Devices** tab, select **SEA-DEV1**.

1. Select **Sync** from the device actions toolbar, then select **Yes**.

1. Wait for the sync to complete (typically 1–2 minutes).

1. Refresh the page and verify the **Last check-in** timestamp updated.

   > [!NOTE]
   > The Sync action forces the device to check in with Intune immediately, retrieve new policies, and report current status. This is useful when troubleshooting policy deployment delays.

**You have successfully forced a device sync from the Troubleshooting blade.**

---

### Task 4: Investigate compliance state and Conditional Access (Report-only) impact

The `CA - Require compliant device (Pharmacy pilot)` Conditional Access policy you created in **Exercise 2 Task 4** is running in **Report-only** mode — it doesn't enforce, but it does log what *would* have happened on every sign-in. You'll inspect those logs now to see the policy's impact before flipping it to **On** in **Lab 04 Exercise 6**.

1. On the **Troubleshooting + support | Troubleshoot** page, with a pilot-cohort user selected (Megan Bowen or another `sg-Intune-Pilot-Users` member), scroll to the **Compliance** section.

1. Note the user's device compliance state. A **Not compliant** or **Not evaluated** state means the CA policy in enforcement mode would block the sign-in.

1. Open a new browser tab to **https://entra.microsoft.com** → **Monitoring & health** → **Sign-in logs**.

1. On the **User sign-ins (interactive)** tab, select **Add filter** to filter by **User principal name** for the same pilot user, and set the **Date range** filter to **Last 24 hours**.

1. Select a sign-in entry where the **Application** column shows an actual cloud app or resource — for example **Microsoft Intune admin center**, **Office 365**, or **Microsoft 365 admin portal**. Avoid entries for **Device Registration Service** or similar system/enrollment apps.

   > [!NOTE]
   > Conditional Access only evaluates sign-ins to cloud resources — it doesn't apply to the local Windows sign-in process, Windows Hello for Business, or device registration/enrollment sign-ins ("bootstrap scenarios," exempt to avoid a circular dependency). If you pick one of those entries, the Conditional Access tab shows **Not applicable** regardless of the policy's configuration — that's expected for that entry, not a sign the policy is misconfigured. Pick a different entry with a real cloud-app resource to see an actual **Report-only** result.

1. Select any recent sign-in entry to open its **Activity details: Sign-ins** pane.

1. Switch to the **Conditional Access** tab in the details pane. You should see `CA - Require compliant device (Pharmacy pilot)` listed with a **Result** of **Report-only: Success**, **Report-only: Failure**, **Report-only: Not applied**, **Report-only: User action required**, or **Not applied**.

   > [!NOTE]
   > **Report-only result decoder:**
   > - **Success** — the user/device would have satisfied the grant (e.g., device is compliant). Enforcing the policy now would not block this sign-in.
   > - **Failure** — the grant requirement (compliance) was *not* met. Enforcing now **would block** this sign-in. This is what you're watching for.
   > - **Not applied** — the policy didn't match the sign-in's user/app/condition criteria. Expected for non-pilot users.
   > - **User action required** — the user could remediate (e.g., complete MFA). Less common for compliance-only grants.
   > - **Not applicable** — this specific sign-in event was exempt from Conditional Access entirely (Windows Hello for Business, device registration, or another bootstrap scenario) — it never gets evaluated, in report-only mode or otherwise. If most of the pilot user's sign-ins show this, pick an entry tied to an actual cloud app instead.

1. Open a second sign-in entry from a user *outside* `sg-Intune-Pilot-Users` (e.g., the admin account). Confirm the CA policy shows **Report-only: Not applied** — because the policy is scoped only to the pilot group.

   > [!IMPORTANT]
   > Report-only → On is a deliberate, two-step rollout: watch the report for at least a few hours (production: days), confirm the **Failure** count is what you expect (i.e., only non-compliant devices), and only then switch to **On**. You'll perform the switch in **Lab 04 Exercise 6** after Lab 04's endpoint security policies have made more devices verifiably compliant.

**You have successfully investigated the Conditional Access policy's report-only impact and the compliance state behind it.**

---

## Lab Summary

Congratulations! You've completed Lab 02: Manage and maintain devices.

In this lab, you accomplished the following:

**Exercise 1: Create configuration profiles**
- Created a Settings Catalog profile for power management (tagged with `Pharmacy`)
- Created a Device Restrictions profile using a built-in template (tagged with `Pharmacy`)
- Created compound and simple assignment filters and applied one in **exclude** mode
- Intentionally created two conflicting camera profiles for the pilot cohort (resolved in Exercise 6)

**Exercise 2: Configure compliance policies**
- Created a Windows compliance policy with device health and security requirements (tagged with `Pharmacy`)
- Configured grace periods and notification actions for noncompliance
- Created a Conditional Access policy (`CA - Require compliant device (Pharmacy pilot)`) in **Report-only** mode — switched to **On** in Lab 04 Exercise 6
- Monitored compliance policy results for enrolled devices

**Exercise 3: Analyze Group Policy Objects**
- Imported a Group Policy backup XML into Group Policy analytics
- Reviewed the migration readiness report to identify supported/unsupported settings
- Exported the analysis results for planning

**Exercise 4: Configure Windows Update management**
- Created a pilot update ring with no deferrals for early adopters (tagged with `Pharmacy`)
- Created a standard update ring with 7-day quality and 14-day feature update deferrals
- Created a Feature update profile pinning the fleet to Windows 11 24H2 (with the pilot cohort excluded so they run ahead)
- Created an Expedited Quality update policy for out-of-band security patches
- Monitored Windows Update deployment status across devices

**Exercise 5: Enable Endpoint analytics and proactive remediations**
- Enabled Endpoint analytics to monitor device performance and user experience
- Enabled Windows license verification, a tenant-level prerequisite for remediations
- Created a proactive remediation script package to detect and clear old temp files
- Monitored remediation execution results

**Exercise 6: Use the Troubleshooting blade**
- Investigated a user's device status and policy assignments
- Diagnosed and resolved a real policy conflict using **Per-setting status**
- Forced a device sync to retrieve new policies immediately
- Inspected the Conditional Access policy's **Report-only** impact via sign-in logs

**Key Takeaways:**
- Configuration profiles can be created using Settings Catalog (granular control) or templates (pre-configured bundles)
- Assignment filters refine policy targeting without creating additional groups
- Compliance policies with grace periods provide users time to remediate issues before access is blocked
- Group Policy analytics helps plan on-premises-to-cloud migration by identifying supported settings
- Windows Update rings enable phased rollouts with deferrals for stability
- Endpoint analytics and proactive remediations enable proactive device management and issue resolution
- The Troubleshooting blade consolidates device, policy, and app status for efficient troubleshooting

**Next Steps:**
In Lab 03, you'll deploy applications to managed devices using Microsoft Store apps, Win32 packages, Microsoft 365 Apps, and App Protection Policies.

---

**END OF LAB**
