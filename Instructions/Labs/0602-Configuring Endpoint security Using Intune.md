# Practice Lab: Configuring Endpoint security using Intune

## Summary

In this lab, you will create a policy to configure Microsoft Defender for managed devices in Intune.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

### Scenario

You've been asked to ensure that the Contoso Developers Group have Microsoft Defender correctly configured. It's been requested that:
* Tamper protection be prevented
* Hide the Account protection, App and browser control, Device security, Device performance and health, and Family options areas in the Windows Security app
* Company name and phone number must be added. 
* Real-time protection, Remediation, and scan settings are also to be configured.

Settings will be verified by testing on an enrolled device, SEA-WS1 and a non-enrolled device, SEA-CL1.

### Task 1: Configure Windows Security Experience in Intune

1. Sign in to **SEA-SVR1** as **Contoso\\Administrator** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Endpoint security**, then select **Antivirus**.

6. On the **Endpoint security |Antivirus** pane, select **Create Policy**.

7. In the **Create a profile** pane, for **Platform**, select **Windows 10, Windows 11, and Windows Server**. 

8. In the **Profile** list, select **Windows Security experience**. Then select **Create**.


8. On the Basics tab, in the **Name** field, enter **Windows Security Settings**. Select **Next**.

9. Under **Defender**, configure the following settings:
    - TamperProtection (Device): **On**

10. Under **Windows Defender Security Center**, configure the following settings:
     - Disable Account Protection UI: **Enable**
     - Disable App Browser UI: **Enable**
     - Disable Device Security UI: **Enable**
     - Disable Family UI: **Enable**
     - Disable Health UI: **Enable**

11. Next to **Enable Customized Toasts** select **Enable**.

12. In the **Company name** field, select **Configured**, and then enter **Contoso IT**.

13. For **Phone**, select **Configured** and then enter **555-1234** and then select **Next**.

14. On the **Scope tags** page, select **Next**.

15. On the **Assignments** tab, under **Included groups** select **Add groups**. Choose the **Contoso Developer Devices** group, click **Select** and then select **Next**.

16. On the **Review + create** tab, review the information and select **Create**.

### Task 2: Configure Microsoft Defender Antivirus policy in Intune

1. On the **Endpoint security |Antivirus** pane, select **Create Policy**.

2. In the **Create a profile** pane, for **Platform**, select **Windows 10, Windows 11, and Windows Server**. 

3. In the **Profile** list, select **Microsoft Defender Antivirus**, then select **Create**.

4. On the **Basics** tab, in the **Name** field, enter **Microsoft Defender Antivirus Settings**. Select **Next**.

5. On the **Configuration settings** tab, configure the following settings:

   - Allow Intrusion Prevention System: **Allowed**
   - Allow scanning of all downloaded files and attachments: **Allowed**
   - Allow Realtime Monitoring: **Allowed**
   - Check For Signatures Before Running Scan: **Enabled**
   - Days to Retain Cleaned Malware: **60**

   - Schedule Quick Scan Time: **60** (represents 1:00AM)
   - Submit samples consent: **Send safe samples automatically**

6. On the **Configuration settings** tab, select **Next**.

7. On the **Assignments** tab, under **Included groups** select **Add groups**. 

8. Choose the **Contoso Developer Devices** group and then choose **Select** and then select **Next**.

9. On the **Scope tags** page, select **Next**.

10. On the **Review + create** tab, review the information and select **Create**.

### Task 3: Sync the managed devices

1. In the Microsoft Endpoint Manager admin center, select **Devices** and then select **All devices**.  

2. On the **Devices | All devices** pane, select **SEA-WS1** and then on the **SEA-WS1** blade, select **Sync** on the toolbar, and then select **Yes**. 

   > Wait for 3-4 minutes for the sync to complete.

3. Close Microsoft Edge.

### Task 4: Verify the configuration

1. Switch to **SEA-CL1**.

2. If necessary, sign in as **Contoso\Administrator** with the password of **Pa55w.rd**.

3. On **SEA-CL1**, select **Start**, type **Windows Security**, and then under the Windows Security icon select **Open**.

   > Notice that all security options are displayed. This is because SEA-CL1 is not enrolled to Intune.

4. Close **Windows Security** and sign out of SEA-CL1.

5. Switch to **SEA-WS1**, and sign in as as **Aaron Nicholls** with the PIN: **102938**.

6. Select **Start**, type **Windows Security**, and then under the Windows Security icon select **Open**.

   > Notice that all of the restricted areas as configured in the Intune policy are not displayed. SEA-WS1 is enrolled in Intune, which has applied the security settings.

7. Close **Windows Security** and sign out of **SEA-WS1**.

**Results**: After completing this exercise, you will have successfully created and applied a policy to configure Microsoft Defender for managed devices in Intune.

**END OF LAB**
