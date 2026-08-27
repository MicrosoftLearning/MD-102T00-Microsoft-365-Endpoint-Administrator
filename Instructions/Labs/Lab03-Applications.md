---
lab:
   title: 'Lab 03: Manage applications'
   description: 'In this lab, you deploy Microsoft Store apps, package and deploy Win32 applications, configure Microsoft 365 Apps, use the Enterprise App Catalog, configure app supersedence, and apply app protection policies.'
   duration: 100 minutes
   level: 200
   islab: true
   primarytopics:
      - Microsoft Intune
      - Windows
      - Microsoft Store
      - Enterprise App Catalog
---

# Lab 03: Manage applications

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices enrolled and managed (Labs 01-02), you now need to deploy applications to users and devices. You'll use multiple deployment methods: Microsoft Store apps (modern apps), Win32 packages (legacy applications), Microsoft 365 Apps (productivity suite), and the Enterprise App Catalog (curated third-party apps). You'll also configure App Protection Policies to secure corporate data on mobile and unenrolled devices.

By the end of this lab, you'll have:
- Deployed a Microsoft Store app
- Packaged and deployed a Win32 application with custom detection rules (tagged with the `Pharmacy` scope tag from Lab 01)
- Deployed Microsoft 365 Apps with update channel configuration
- Added and assigned an app from the Enterprise App Catalog
- Configured app supersedence to automatically upgrade an application (still scoped to the pilot cohort and tagged `Pharmacy`)
- Created an App Protection Policy for mobile devices
- Monitored app deployment status, troubleshot failures, and diagnosed an intentional app-assignment conflict

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
- Internet access on **SEA-DEV1** to download the official 7-Zip installer directly from **7-zip.org** for **Exercise 2** — there's no pre-packaged app asset; you download the real installer yourself
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Exercise 4 (Enterprise App Catalog)

---

## Exercise 1: Deploy Microsoft Store apps

### Scenario

Microsoft Store apps are modern Windows applications distributed through the Microsoft Store. Intune can deploy Store apps to managed devices without requiring users to access the Store directly.

### Task 1: Add a Microsoft Store app

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. If prompted to stay signed in, select **No**.

1. In the **Microsoft Intune admin center**, select **Apps**, and then select **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows**, then set **App type** to **Microsoft Store app (new)**. Select **Select**.

   > [!NOTE]
   > The portal flow is a two-step picker: choose Platform first (Windows / iOS/iPadOS / macOS / Android), then the App type list filters to that platform. The "new" Microsoft Store app type uses the Microsoft Store for Business backend and provides better reliability than the legacy connector.

1. On the **App information** tab, select **Search the Microsoft Store app (new)**.

1. In the **Search the Microsoft Store app (new)** pane, search for `Microsoft To Do`.

1. Select **Microsoft To Do: Lists, Tasks & Reminders** from the search results.

1. Select **Select**.

1. On the **App information** page, verify the app details:
   - **Name:** Microsoft To Do
   - **Publisher:** Microsoft Corporation
   - **Description:** (auto-populated from Store)

1. Select **Next**, then select **Next** again to skip the **Scope tags** tab.

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

   > [!NOTE]
   > Assigning as "Required" means the app will install automatically on all devices in the group. "Available" would make it visible in the Company Portal for user-initiated installation.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully added and assigned a Microsoft Store app.**

---

### Task 2: Verify app installation on SEA-DEV1

1. On **SEA-DEV1**, wait 5–10 minutes for the app to install automatically.

   > [!NOTE]
   > Intune checks for new app assignments every 8 hours by default, or when the device syncs. You can force a sync to speed up installation.

1. To force a device sync, open **Settings** (press `Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select the **Connected to Contoso** entry (or **Connected to <TenantPrefix>** if the display name differs).

1. Select **Info** → Scroll down and select **Sync**.

1. Wait for the sync to complete (typically 1–2 minutes).

1. After sync, open the **Start menu** and search for `Microsoft To Do`.

1. Verify the app appears in the search results and can be launched.

**You have successfully verified Microsoft Store app installation.**

---

## Exercise 2: Package and deploy a Win32 application

### Scenario

Win32 apps are traditional Windows desktop applications (.exe, .msi installers). You'll package a Win32 app using the Microsoft Win32 Content Prep Tool, create a detection rule, and deploy it to managed devices.

### Task 1: Prepare the Win32 app package

> [!IMPORTANT]
> **Download the real installer yourself — don't use a pre-packaged app asset.** Embedding a compiled `.exe`/`.msi` in training content is a supply-chain risk: its provenance can't be verified, and it's the kind of artifact a security review would (rightly) flag. This task has you download the **official** 7-Zip installer directly from the vendor, not a repackaged "portable" build from a third-party site.

1. On **SEA-DEV1**, verify the Win32 Content Prep Tool is available at `C:\Program Files\IntuneWinAppUtil\IntuneWinAppUtil.exe`.

   > [!NOTE]
   > If the tool is not present, download it from https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool/releases and extract to the specified path.

1. Open **Microsoft Edge** and navigate to **https://www.7-zip.org/download.html** — the official 7-Zip download page (published by Igor Pavlov, the actual author).

1. Download the current **64-bit Windows x64 .msi** package (not the .exe installer, and not any "portable" edition from a third-party mirror).

1. Create the source folder and move the downloaded MSI into it:

   ```powershell
   New-Item -ItemType Directory -Path "C:\LabAssets\Win32-App\Source" -Force
   Move-Item "$env:USERPROFILE\Downloads\7z*.msi" "C:\LabAssets\Win32-App\Source\"
   ```

1. Note the exact downloaded filename (it changes with each 7-Zip release, e.g. `7z2408-x64.msi`) — you'll need it for the next command.

   > [!NOTE]
   > This lab uses `7z-portable.exe` as the example payload. If you use a different installer (for example, Notepad++ `npp.8.9.7.Installer.x64.exe`), substitute the **filename**, **app name/publisher**, **install/uninstall commands**, and **detection path** consistently throughout Exercises 2, 5, and 7.

1. Open **Terminal (Admin)** (right-click Start → Terminal (Admin)). On Windows 11, this opens Windows Terminal with a PowerShell tab.

1. On the **Do you want to allow this app to make changes to your device?** prompt, select **Yes**.

1. Navigate to the Win32 Content Prep Tool directory:

   ```powershell
   cd "C:\Program Files\IntuneWinAppUtil"
   ```

1. Run the content prep tool to package the app (replace `<filename>` with the actual .msi filename from the previous step):

   ```powershell
   .\IntuneWinAppUtil.exe -c "C:\LabAssets\Win32-App\Source" -s "<filename>.msi" -o "C:\LabAssets\Win32-App\Output"
   ```

   - `-c`: Source folder containing the app files
   - `-s`: Setup file (the MSI installer)
   - `-o`: Output folder for the .intunewin package

   > [!NOTE]
   > Because the setup file is an MSI, the Content Prep Tool automatically reads the MSI's product code, version, and other metadata and embeds it in the .intunewin package — this is what enables MSI-based automatic detection in Task 2, instead of a manual file-path check.

1. Wait for the packaging to complete (typically 10–30 seconds).

1. Verify the .intunewin file was created (replace `<filename>` with the same filename):

   ```powershell
   Test-Path "C:\LabAssets\Win32-App\Output\<filename>.intunewin"
   ```

   The output should return **True**.

**You have successfully packaged a Win32 app using the Intune Win32 Content Prep Tool.**

---

### Task 2: Add the Win32 app to Intune

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Select**.

1. On the **App information** tab, select **Select app package file**.

1. In the **App package file** pane, select the folder icon next to **Select a file**, and navigate to `C:\LabAssets\Win32-App\Output\`.

1. Select the `.intunewin` file you created in Task 1 and select **OK**.

   > [!NOTE]
   > Because the source was an MSI, Intune reads the **Name**, **Description**, **Publisher**, and **Version** fields directly from the package metadata and pre-fills them on the next page. Review them for accuracy rather than typing them from scratch.

1. On the **App information** page, confirm the auto-populated fields look correct 

1. **Publisher** should read **Igor Pavlov**, and adjust the **Description** if you want:
   - **Description:** `7-Zip file archiver for Windows`

1. Select **Next**.

1. On the **Program** page, the **Install command** and **Uninstall command** are auto-populated from the MSI package metadata — confirm they look correct:
   - **Install command:** `msiexec /i "<filename>.msi" /qn`
   - **Uninstall command:** `msiexec /x "{<product-code-GUID>}" /qn`

   > [!NOTE]
   > `/qn` performs a silent MSI installation (no user prompts). The uninstall command references the MSI's **product code** (a GUID), not the original filename — Windows Installer can uninstall an MSI-based app by product code alone, even if the original installer file is gone from the device.

1. Confirm **Install behavior** is set to **System** (already the default for this package).

1. Change **Device restart behavior** from the pre-selected default (**App install may force a device restart**) to **Determine behavior based on return codes**.

   > [!NOTE]
   > Leave **Installer type** / **Uninstaller type** (both **Command line**), **Installation time required (mins)**, **Allow available uninstall**, and the **Return codes** table (0 and 1707 = Success, 3010 = Soft reboot, 1641 = Hard reboot) as their pre-populated defaults — these come from Intune's built-in MSI handling, not from anything you need to configure.

1. Select **Next**.

1. On the **Requirements** page, configure:
   - **Check operating system architecture:** **Yes. Specify the systems the app can be installed on.**
   - Under the architecture checkboxes, check **Install on x64 system** only (leave **x86** and **ARM64** unchecked)
   - **Minimum operating system:** Windows 10 1607

   > [!NOTE]
   > Leave **Disk space required**, **Physical memory required**, **Minimum number of logical processors required**, and **Minimum CPU speed required** blank — none apply to this app. **Configure additional requirement rules** stays empty too.

1. Select **Next**.

1. On the **Detection rules** tab, configure:
   - **Rules format:** Manually configure detection rules

1. Select **+Add** under **Detection rules**.

1. In the **Detection rule** pane, configure:
   - **Rule type:** MSI
   - **MSI product code:** Leave as auto-populated (Intune reads this from the .intunewin package's embedded MSI metadata)

   > [!NOTE]
   > This is the whole point of packaging an MSI instead of a portable/manual installer: Intune already knows the product code from the package, so detection is a reliable version check against the real Windows Installer registration — not a fragile "does this file exist" guess.

1. Select **OK**.

1. Select **Next**.

1. On the **Dependencies** tab, select **Next** (no dependencies required).

1. On the **Supersedence** tab, select **Next** (will configure supersedence in a later task).

1. On the **Scope tags** tab, select **+ Select scope tags**, add **Pharmacy** (created in **Lab 01 Exercise 2 Task 6**), select **Select**, then select **Next**.

   > [!NOTE]
   > 7-Zip is the canonical archive tool for the Contoso clinical document workflow (research-data exports, anonymized DICOM bundles). Tagging the deployment with `Pharmacy` keeps it visible to the Pharmacy Helpdesk role (assigned in **Lab 05 Exercise 3**).

1. On the **Assignments** tab, under **Required**, select **+Add group**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully added a Win32 app with a custom detection rule.**

---

### Task 3: Monitor Win32 app installation

1. On **SEA-DEV1**, force a device sync:
   - **Settings** → **Accounts** → **Access work or school** → **Connected to Contoso** → **Info** → **Sync**

1. Wait 10–15 minutes for the app to install.

   > [!NOTE]
   > Win32 app installation can take longer than Store apps because Intune must download the package, run the installer, and verify the detection rule.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip**.

1. Select **Device install status** from the left navigation.

1. Review the installation status for each device:
   - **Installed:** App successfully installed and detection rule passed
   - **In progress:** Installation is running
   - **Failed:** Installation failed (review error code and message)
   - **Not applicable:** Device not targeted by the assignment

1. If installation failed, select the failed device to view detailed error information.

**You have successfully monitored Win32 app installation status.**

---

## Exercise 3: Deploy Microsoft 365 Apps

### Scenario

Microsoft 365 Apps (formerly Office 365 ProPlus) provide Word, Excel, PowerPoint, Outlook, and other productivity tools. You'll deploy the suite to managed devices with a specific update channel configuration.

### Task 1: Add Microsoft 365 Apps

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Microsoft 365 Apps for Windows 10 and later**. Select **Select**.

1. On the **App suite information** tab, configure:
   - **Suite Name:** `Microsoft 365 Apps (Current Channel)`
   - **Suite Description:** `Microsoft 365 Apps with Current Channel updates`

1. Select **Next**.

1. On the **Configure app suite** page, leave **Configuration settings format** set to **Configuration designer**.

1. Under **Select Office apps**, open the dropdown and check:
   - **Excel**
   - **Outlook**
   - **PowerPoint**
   - **Teams**
   - **Word**

   > [!NOTE]
   > There's no standalone "OneDrive" entry in this list — Excel, Outlook, OneNote, PowerPoint, Access, Publisher, Skype for Business, Teams, and Word are the only options. Leave **Select other Office apps (license required)** at **0 selected** — that dropdown is for apps like Project and Visio that need their own license, not part of this deployment.

1. Under **App suite information**, configure:
   - **Architecture:** **64-bit** (toggle, already selected by default)
   - **Default file format:** **Office Open XML Format** — this field is required; the page shows a validation error until you pick one
   - **Update channel:** **Current Channel (Preview)** — also required
   - **Remove other versions:** Yes (default)
   - **Version to install:** Latest (default; leave **Specific version** disabled)

1. Under **Properties**, configure:
   - **Use shared computer activation:** No (default)
   - **Accept the Microsoft Software License Terms on behalf of users:** Yes
   - **Install background service for Microsoft Search in Bing:** No

1. Scroll down and, under **Languages**, select **English (United States)**.

   > [!NOTE]
   > Current Channel receives new features as soon as they're released. Monthly Enterprise Channel provides monthly updates with a longer lead time for testing.

1. Select **Next**.

1. On the **Scope tags** page, select **Next** (no scope tag needed for this deployment).

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully configured and assigned Microsoft 365 Apps.**

---

### Task 2: Monitor Microsoft 365 Apps installation

1. On **SEA-DEV1**, force a device sync.

1. Wait 15–30 minutes for Microsoft 365 Apps to download and install.

   > [!NOTE]
   > Microsoft 365 Apps is a large download (~3 GB) and installation can take 20–40 minutes depending on network speed and device performance. For lab purposes, you can proceed to the next exercise and check installation status later.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **Microsoft 365 Apps (Current Channel)**.

1. Select **Device install status** from the left navigation.

1. Review the installation progress for each device.

1. After installation completes, on **SEA-DEV1**, open the **Start menu** and verify the following apps are present:
   - **Excel**
   - **Word**
   - **PowerPoint**
   - **Outlook**

**You have successfully deployed and monitored Microsoft 365 Apps installation.**

---

## Exercise 4: Use the Enterprise App Catalog

### Scenario

The Enterprise App Catalog (part of Microsoft Intune Suite) provides a curated library of third-party applications with pre-configured installers, detection rules, and icons. You'll add an app from the catalog and deploy it to devices.

> [!NOTE]
> The **Enterprise App Catalog** is part of **Microsoft Intune Enterprise Application Management**, a Microsoft Intune Suite capability. The Suite trial was activated in **Lab 01** prerequisites, so this exercise is fully hands-on.

### Task 1: Browse the Enterprise App Catalog

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Enterprise App Catalog app**. Select **Select**.

   > [!NOTE]
   > Enterprise App Catalog app is now generally available (the "(preview)" suffix that appeared earlier has been dropped). It's part of **Enterprise App Management**, an Intune Suite capability — active because of the Suite trial from Lab 01 prerequisites. If this option doesn't appear, the Suite trial may not have fully provisioned yet. Wait 5–10 minutes after activation and refresh — capability tiles can take a few minutes to surface after the trial flips to **Active**.

1. On the **Select app** page, select **Search the Enterprise App Catalog** to browse the available apps in the catalog.

   The catalog includes popular enterprise apps such as:
   - **Google Chrome**
   - **Mozilla Firefox**
   - **Zoom**
   - **Adobe Acrobat Reader**
   - **VLC Media Player**
   - **Notepad++**

1. Search for or select **Google Chrome** from the list.

1. Select **Next**.

1. On the **Configuration** tab, use **Search for a branch** if you want a different release, or leave the default row selected. Confirm the row shows:
   - **Package name:** `googlechromestandaloneenterprise64.msi`
   - **Language:** en-US
   - **Architecture:** x64
   - **Version:** (current release, e.g. `150.0.7871.129`)

   > [!NOTE]
   > The Enterprise App Catalog packages the same official installer Google publishes — this tab just lets you pick which branch/architecture/language build to deploy.

1. Select **Next**.

1. On the **Updates** tab, note the banner: *"This selection is a one-time choice for this app. You will need to create a new app to make a different selection."*

1. Under **Update method**, select **Update with supersedence**.

   > [!NOTE]
   > **Automatically update** keeps the app current directly from the catalog but resets and blocks custom install/uninstall scripts. **Update with supersedence** lets you keep custom settings and push new versions through a guided supersedence relationship instead — consistent with how you'll manage the `7-Zip` app in **Exercise 5**.

1. Review the read-only **App information** (App name, Package name, Version, Publisher, Architecture, Application size, Privacy URL, App store URL) and **App commands** (**Install command**, pre-built as `"%SystemRoot%\System32\msiexec.exe" /i "googlechromestandaloneenterprise64.msi" /qn`) — none of this needs editing.

1. Select **Next**.

1. On the **Configuration** tab, select the package **Google Chrome**.

1. Select **Next**.

1. On the **Updates** tab, select **Select**.

**You have successfully browsed the Enterprise App Catalog and selected an app.**

---

### Task 2: Configure and assign the app

1. On the **App information** page, review the pre-populated details:
   - **Name:** Google Chrome
   - **Description:** (auto-populated)
   - **Publisher:** Google
   - **Installation command:** (pre-configured, from the Configuration/Updates steps you just completed)
   - **Detection rule:** (pre-configured)

1. Select **Next**.

1. On the **Program** page, review the auto-populated fields — none need editing:
   - **Installer type:** Command line
   - **Install command:** `"%SystemRoot%\System32\msiexec.exe" /i "googlechromestandaloneenterprise64.msi"` (matches the Install command you reviewed on the **Updates** tab in Task 1)
   - **Uninstaller type:** Command line
   - **Uninstall command:** `"%SystemRoot%\System32\msiexec.exe" /X {<product-code-GUID>}`
   - **Installation time required (mins):** 60
   - **Allow available uninstall:** Yes
   - **Install behavior:** grayed out/non-editable for this app — leave as is
   - **Device restart behavior:** **Determine behavior based on return codes** — already the default here, unlike the Win32 app you configured manually in **Exercise 2**

   > [!NOTE]
   > The banner at the top of this page ("This app can update itself...") is the Enterprise App Catalog reminding you that Chrome self-updates once installed — the same self-updating behavior you accounted for by choosing **Update with supersedence** in Task 1.

1. Select **Next**.

1. On the **Requirements** page, review the pre-configured requirements and select **Next**.

1. On the **Detection rules** tab, review the pre-configured detection rule:
   - **Rule type:** File or registry-based detection
   - **Path/Code:** Checks for Chrome installation path

1. Select **Next**.

1. On the **Scope tags** page, select **Next** (no scope tag needed for this app).

1. On the **Supersedence** page, select **Next** (no supersedence relationship needed — this is the first version of this app).

1. On the **Assignments** page, under **Available for enrolled devices**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

   > [!NOTE]
   > Assigning as "Available" makes the app visible in the Company Portal app, allowing users to install it on-demand. This is useful for optional software.

1. Select **Next**.

1. On the **Review + create** tab, select **Add app**.

**You have successfully added and assigned an app from the Enterprise App Catalog.**

---

### Task 3: Verify app availability in the Company Portal

1. On **SEA-DEV1**, open the **Start menu** and search for `Company Portal`.

1. Launch the **Company Portal** app.

   > [!NOTE]
   > If the **Company Portal** app isn't available on the device, open **Microsoft Edge** and navigate to **https://apps.microsoft.com/detail/9wzdncrfj3pz?hl=en-GB&gl=PT** to install the Company Portal app from the Microsoft Store.

1. Sign in as **MeganB@<TenantPrefix>.OnMicrosoft.com** (if not already signed in).

1. Navigate to the **Apps** section.

1. Verify **Google Chrome** appears in the available apps list.

1. Select **Install** to install the app.

1. Wait for installation to complete.

1. Open the **Start menu** and verify **Google Chrome** is present.

**You have successfully installed an app from the Company Portal.**

---

## Exercise 5: Configure app supersedence

### Scenario

App supersedence allows you to automatically upgrade or replace applications. When a user has an older version installed, Intune automatically uninstalls it and installs the newer version.

### Task 1: Create a second version of the Win32 app

For this task, you'll simulate a new version by creating a second Win32 app entry from the same package.

> [!NOTE]
> In production, "v2.0" would be a genuinely newer installer with a different MSI product code. For lab purposes, you're reusing the **same** `.intunewin` package you built in **Exercise 2 Task 1** under a new app name — this is enough to demonstrate the supersedence *mechanic* (Intune uninstalling one app object and installing another) without needing to source two real 7-Zip releases.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **+ Create**.

1. Set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Create**.

1. Walk through the wizard exactly as you did in **Exercise 2 Task 2** (**Program**, **Requirements**, **Detection rules**, **Dependencies**, **Assignments**), with these differences:

   - **App information:** select **Select app package file** and upload the same `<filename>.intunewin` package from `C:\LabAssets\Win32-App\Output\`, then set **Name** to `7-Zip v2.0` and **Description** to `Updated version of 7-Zip` (**Publisher** stays **Igor Pavlov**, auto-populated).
   - **Supersedence:** select **Uninstall previous version** and select **Next**. This removes the original **7-Zip** app before installing **7-Zip v2.0**.

     > [!NOTE]
   - **Scope tags:** add **Pharmacy** (same as the original app) — keeps Pharmacy delegation consistent across both versions.
   - **Assignments:** assign **Required** to **sg-Intune-Pilot-Users** (same as the original app).

1. On the **Review + create** tab, select **Create**.

**You have successfully configured app supersedence to automatically upgrade from v1 to v2.**

---

### Task 2: Verify app supersedence behavior

1. On **SEA-DEV1**, force a device sync.

1. Wait 10–15 minutes for Intune to detect the supersedence relationship and upgrade the app.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip v2.0**.

1. Select **Device install status** and verify SEA-DEV1 shows **Installed**.

1. Navigate to **7-Zip** (the original app) and select **Device install status**.

1. Verify the status shows **Superseded** or **Not installed**.

**You have successfully verified app supersedence automatically replaced the old app with the new version.**

---

## Exercise 6: Create an App Protection Policy

### Scenario

App Protection Policies (APP) secure corporate data on mobile devices and BYOD (bring-your-own-device) scenarios without requiring full device enrollment. You'll create an APP for iOS/Android that prevents copy/paste, requires a PIN, and enforces conditional access.

### Task 1: Create an iOS App Protection Policy

1. In the **Microsoft Intune admin center**, select **Apps**, and then select **Protection**.

1. Select **+ Create** → **iOS/iPadOS** to create a new policy.

1. On the **Basics** tab, configure:
   - **Name:** `APP - iOS Data Protection`
   - **Description:** `Protects corporate data in Microsoft apps on iOS devices`

1. Select **Next**.

1. On the **Apps** tab, select **+ Select public apps**.

1. In the app picker, search for and select:
   - **Microsoft Outlook**
   - **Microsoft Teams**
   - **Microsoft Word**
   - **Microsoft Excel**
   - **Microsoft PowerPoint**
   - **Microsoft OneDrive**
   - **Microsoft 365 Copilot**

1. Select **Select**.

1. Select **Next**.

1. On the **Data protection** tab, configure:
   - **Data transfer:**
     - **Send org data to other apps:** Policy managed apps
     - **Receive data from other apps:** Policy managed apps
     - **Save copies of org data:** Block
     - **Allow user to save copies to selected services:** OneDrive for Business, SharePoint
     - **Restrict cut, copy, and paste between apps:** Policy managed apps with paste in
   - **Encryption:**
     - **Encrypt org data:** Require
   - **Functionality:**
     - **Sync policy managed app data with native apps or add-ins:** Block
     - **Printing org data:** Block
     - **Restrict web content transfer with other apps:** Microsoft Edge

1. Select **Next**.

1. On the **Access requirements** tab, configure:
   - **PIN for access:** Require
   - **PIN type:** Numeric
   - **Select Minimum PIN length:** 6
   - **Override biometrics with PIN after timeout:** Require
   - **Work or school account credentials for access:** Require
   - **Recheck the access requirements after (minutes of inactivity):** 30

1. Select **Next**.

1. On the **Conditional launch** page, review the default conditions:
   - **App conditions:**
     - **Max PIN attempts:** 5 (Action: Reset PIN)
     - **Offline grace period:** 1440 minutes (Action: Block access)
     - **Offline grace period:** 90 days (Action: Wipe data)
   - **Device conditions:**
     - **Jailbroken/rooted devices:** (Action: Block access)

   > [!NOTE]
   > These four rows are pre-populated defaults — you don't need to add anything. The **Select one** dropdowns at the bottom of each table (App conditions / Device conditions) are there if you want to add more conditions (e.g., a minimum OS version), but that's optional and not required for this lab.

1. Select **Next** and skip **Scope tags**.

1. On the **Assignments** page, under **Included groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

   > [!NOTE]
   > There's no built-in "All users" or "All devices" virtual assignment on this page — **Included groups** and **Excluded groups** both only offer **Add groups**. This lab scopes the policy to the same pilot cohort you've used throughout Lab 03 rather than a blanket assignment; in production you'd typically create a group dedicated to App Protection Policy targeting.

1. Select **Next**.

1. On the **Review + create** tab, select **Create**.

**You have successfully created an iOS App Protection Policy.**

---

### Task 2: Create an Android App Protection Policy

1. On the **App | Protection** page, select **+ Create** → **Android** to create a new policy.

1. On the **Basics** page, configure:
   - **Name:** `APP - Android Data Protection`
   - **Description:** `Protects corporate data in Microsoft apps on Android devices`

1. Select **Next**.

1. On the **Apps** tab, select **+ Select public apps**.

1. Search for and select the same Microsoft apps as the iOS policy (Outlook, Teams, Word, Excel, PowerPoint, OneDrive).

1. Select **Select** and then select **Next**.

1. On the **Data protection** page, configure:
   - **Backup org data to Android backup services:** Allow (default)
   - **Send org data to other apps:** change from the default **All Apps** to **Policy managed apps**
   - **Save copies of org data:** Block
   - **Restrict cut, copy, and paste between apps:** Policy managed apps with paste in
   - **Transfer telecommunication data to:** Any dialer app (default)
   - **Transfer messaging data to:** Any messaging app (default)
   - **Encrypt org data:** Require (default)
   - **Encrypt org data on enrolled devices:** Require (default)
   - **Sync policy managed app data with native apps or add-ins:** change from the default **Allow** to **Block**
   - **Printing org data:** change from the default **Allow** to **Block**
   - **Restrict web content transfer with other apps:** change from the default **Any app** to **Microsoft Edge**

   > [!NOTE]
   > Leave **Org data notifications** (**Allow**) and **Start Microsoft Tunnel connection on app-launch** (**No**) at their defaults — this lab isn't using Microsoft Tunnel.

1. Select **Next**.

1. On the **Access requirements** page, configure:
   - **PIN for access:** Require (default)
   - **PIN type:** Numeric (default)
   - **Simple PIN:** Allow (default)
   - **Select minimum PIN length:** change from the default **4** to **6**
   - **Biometrics instead of PIN for access:** Allow (default)
   - **Override biometrics with PIN after timeout:** Require (default)
   - **Timeout (minutes of inactivity):** 30 (default)
   - **Class 3 Biometrics (Android 9.0+):** Not required (default)
   - **PIN reset after number of days:** No (default)
   - **Select number of previous PIN values to maintain:** 0 (default)
   - **App PIN when device PIN is set:** Require (default)

   > [!NOTE]
   > Unlike the iOS policy, there's no **Work or school account credentials for access** or **Recheck the access requirements after (minutes of inactivity)** setting on the Android **Access requirements** page — don't look for them here.

1. Select **Next**.

1. On the **Conditional launch** tab, review the default conditions and select **Next**.

1. On the **Scope tags** tab, select **Next**.

1. On the **Assignments** page, under **Included groups**, select **Add groups** and select **sg-Intune-Pilot-Users**.

1. Select **Next** → **Create**.

**You have successfully created an Android App Protection Policy.**

---

### Task 3: Understand App Protection Policy enforcement

App Protection Policies are enforced at the application level, not the device level. Here's how they work:

1. **User installs a managed app** (e.g., Outlook) from the App Store or Google Play.

1. **User signs in with work account** (`user@<TenantPrefix>.onmicrosoft.com`).

1. **Intune recognizes the managed identity** and applies the App Protection Policy.

1. **User is prompted to set a PIN** (6 digits or more).

1. **App Protection controls are enforced**:
   - User cannot copy data from Outlook to personal apps (e.g., Gmail)
   - User cannot save attachments outside OneDrive or SharePoint
   - App data is encrypted at rest
   - App is wiped if device is jailbroken/rooted

1. **Conditional Access integration** (optional): If combined with a Conditional Access policy, non-compliant users are blocked from signing in.

> [!NOTE]
> App Protection Policies do not require device enrollment. They protect corporate data on BYOD devices without giving IT full control of the device.

**You now understand how App Protection Policies enforce data protection on mobile devices.**

---

## Exercise 7: Monitor app deployment and troubleshoot failures

### Scenario

You'll use the Intune admin center to monitor app deployment across all devices, identify failed installations, and troubleshoot common issues.

### Task 1: Review the App overview dashboard

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Overview**.

1. Review the **App protection status** dashboard:
   - **iOS:** Number of users with protected apps
   - **Android:** Number of users with protected apps
   - **Windows:** (App Protection Policies not applicable to Windows)

1. In the **App install status** tile, note the number of **Apps with failures**.

1. Select **App install status** to open the report. The report lists the apps with failures and includes these columns:
   - **App name**
   - **Publisher**
   - **Platform**
   - **Version**
   - **Install failure %**
   - **Device failures**
   - **User failures**

1. Select the **App name** to open the app, then under **Monitor** select **Device install status**.

1. Review the **Status** column for each device (see **Status details** for the reason on failures):
   - **Installed:** The app installed successfully and passed its detection rule.
   - **Failed:** The installation failed — check **Status details** for the error.
   - **Pending:** The installation is in progress or awaiting the next device sync.
   - **Not installed:** The app is not installed on the device.

**You have successfully reviewed the App overview dashboard.**

---

### Task 2: Investigate a failed app installation

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select an app that shows installation failures (e.g., **7-Zip**).

1. Select **Device install status** from the left navigation.

1. Locate a device with status **Failed** and select it.

1. Review the error details:
   - **Error code:** Numeric code (e.g., 0x80070005 = Access Denied)
   - **Error message:** Description of the failure
   - **Last modified:** Timestamp of last installation attempt

1. Common failure reasons and resolutions:
   - **0x80070005 (Access Denied):** App installer requires elevation—set install behavior to "System" instead of "User"
   - **Detection rule not met:** App installed successfully but detection rule failed—verify detection rule logic
   - **Download failed:** Device has no internet connectivity or cannot reach Intune endpoints
   - **Disk space insufficient:** Device does not have enough free space for installation

**You have successfully investigated a failed app installation.**

---

### Task 3: Export app install status to CSV

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Monitor** → **App install status**.

1. Select an app from the list (e.g., **Microsoft 365 Apps (Current Channel)**).

1. On the **Device install status** page, select **Export** from the top toolbar, and then select **Yes** to confirm.

1. Wait for the export to complete (typically 1–2 minutes).

1. Open the exported **.zip** file (for example, `DeviceInstallStatusByApp_<id>.zip`). It contains the CSV report.

1. Open the CSV in **Excel** and review the columns:
   - **Device name**
   - **UserPrincipalName**
   - **Platform**
   - **AppInstallState_Ioc (status)** (Installed, Failed, In Progress)
   - **AppInstallStateDetails (error message)**
   - **Last ModifiedDate**

**You have successfully exported app installation data for reporting.**

---

### Task 4: Diagnose an intentional app-assignment conflict

App assignment intents can collide just like configuration profiles can. The classic example is one admin marking an app **Required** for a broad group while another admin marks the same app **Uninstall** for an overlapping group. Intune flags this in the **App install status** view as a conflict, and neither install nor uninstall completes cleanly. You'll deliberately create this situation, find it, and resolve it.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip** (the v1 app you deployed in Exercise 2 — *not* the v2.0).

1. Select **Properties** from the left navigation, then in the **Assignments** section select **Edit**.

1. Under **Uninstall**, select **+ Add group**.

1. Search for and select **sg-Intune-Pilot-Users** (the same pilot cohort that already has **7-Zip v2.0** assigned as **Required** via supersedence). Select **Select**.

1. Select **Review + save** → **Save**.

   > [!IMPORTANT]
   > You've now told Intune: "Uninstall **7-Zip** from pilot users" AND (via the v2.0 supersedence relationship) "Install **7-Zip v2.0** on pilot users, replacing v1." These two intents partially overlap and produce a conflict.

1. Trigger a sync on **SEA-DEV1** (Settings → Accounts → Access work or school → Sync). Wait 5–10 minutes for Intune to evaluate.

1. In **Apps** → **All apps** → **7-Zip**, select **Device install status**. Locate SEA-DEV1 (or any pilot device) and observe the status — you should see **Conflict** or an explicit failure with an error message indicating multiple intents.

   > [!NOTE]
   > Intune surfaces app conflicts as either **Conflict** in the device install status column, or as a specific error in the per-device drill-in. **App install status** is the single most useful surface for diagnosing app assignment fights, the same way **Per-setting status** is for configuration profile conflicts (Lab 02 Exercise 6).

1. Resolve the conflict. The supersedence path is the correct one (v1 → v2.0 is automatic), so remove the redundant Uninstall assignment on v1:
   - On **7-Zip** → **Properties** → **Assignments** → **Edit**.
   - Under **Uninstall**, hover over **sg-Intune-Pilot-Users** and select the **Remove** icon (trash can).
   - Select **Review + save** → **Save**.

1. Trigger another sync on SEA-DEV1, wait 5–10 minutes, and re-check **Device install status** on **7-Zip v2.0**. Confirm SEA-DEV1 shows **Installed** with no remaining conflict on the v1 app.

   > [!NOTE]
   > In production, the upper-intermediate move is to set up **assignment audits** — review the **Audit logs** for app-assignment edits when you find a conflict to see who added the conflicting intent and when. You'll inspect audit logs in **Lab 05 Exercise 4**.

**You have successfully diagnosed and resolved an app-assignment conflict.**

---

## Lab Summary

Congratulations! You've completed Lab 03: Manage applications.

In this lab, you accomplished the following:

**Exercise 1: Deploy Microsoft Store apps**
- Added a Microsoft Store app (Microsoft To Do) to Intune
- Assigned the app as Required to automatically install on devices
- Verified installation on a managed device

**Exercise 2: Package and deploy a Win32 application**
- Packaged a Win32 app using the Intune Win32 Content Prep Tool
- Created a custom file-based detection rule
- Tagged the deployment with the `Pharmacy` scope tag for delegated administration
- Deployed the app to pilot users and monitored installation status

**Exercise 3: Deploy Microsoft 365 Apps**
- Configured Microsoft 365 Apps with Current Channel updates
- Assigned the suite to all Windows devices
- Monitored the large app deployment process

**Exercise 4: Use the Enterprise App Catalog**
- Browsed the Enterprise App Catalog (Intune Suite feature)
- Added Google Chrome with pre-configured settings and detection rules
- Deployed the app as Available in the Company Portal

**Exercise 5: Configure app supersedence**
- Created a newer version of an app (tagged `Pharmacy`)
- Configured a supersedence relationship to automatically replace the old version
- Verified automatic upgrade behavior on devices

**Exercise 6: Create an App Protection Policy**
- Created iOS and Android App Protection Policies
- Configured data protection controls (copy/paste restrictions, encryption, PIN requirements)
- Understood how APP enforces data protection without device enrollment

**Exercise 7: Monitor app deployment and troubleshoot failures**
- Reviewed the App overview dashboard
- Investigated failed app installations and interpreted error codes
- Exported app install status data to CSV for reporting
- Diagnosed and resolved an intentional Required vs. Uninstall app-assignment conflict

**Key Takeaways:**
- Microsoft Store apps provide modern, lightweight application deployment
- Win32 apps require packaging with the Content Prep Tool and custom detection rules
- Microsoft 365 Apps deployment includes update channel configuration for phased rollouts
- Enterprise App Catalog (Intune Suite) simplifies third-party app deployment with pre-configured installers
- App supersedence automates application upgrades without manual uninstall/reinstall
- App Protection Policies secure corporate data on mobile/BYOD devices without full enrollment
- Scope tags carry through the app surface just like configuration and compliance — tag clinical/regulated apps at create time so delegated admins (Pharmacy Helpdesk, Lab 05) can manage them
- App assignment conflicts (Required vs. Uninstall on overlapping groups) surface in **App install status**; resolve by removing the redundant intent and using audit logs (Lab 05) to find who introduced it
- Intune provides comprehensive monitoring and troubleshooting for app deployment

**Next Steps:**
In Lab 04, you'll protect devices using Microsoft Defender for Endpoint integration, endpoint security policies, BitLocker encryption, Microsoft Tunnel Gateway, and Microsoft Cloud PKI.

---

**END OF LAB**
