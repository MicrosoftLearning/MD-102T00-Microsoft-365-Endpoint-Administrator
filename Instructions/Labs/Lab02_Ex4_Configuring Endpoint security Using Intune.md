# Practice Lab02: Manage Windows Device Configuration

## Summary

In this lab, you will create a policy to configure Microsoft Defender for managed devices in Intune.

## Exercise 4: Configuring Endpoint security using intune

### Scenario

You've been asked to ensure that the Contoso Developers Group have Microsoft Defender correctly configured. It's been requested that:
* Tamper protection be prevented
* Hide the Account protection, App and browser control, Device security, Device performance and health, and Family options areas in the Windows Security app
* Company name and phone number must be added. 
* Real-time protection, Remediation, and scan settings are also to be configured.

Settings will be verified by testing on an enrolled device, SEA-WS1 and a non-enrolled device, SEA-CL1.

### Task 1: Configure Windows Security Experience in Intune

1. Sign in to **SEA-WS1** as **Contoso\\Administrator** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the left navigation pane select **Endpoint security**, then select **Antivirus**.

6. On the **Endpoint security | Antivirus** blade, in the **Summary** tab, select **Create Policy**.

7. In the **Create a profile** blade, for **Platform**, select **Windows**. 

8. In the **Profile** list, select **Windows Security experience** and then select **Create**.

9. In the **Basics** tab, in the **Name** field, enter **Windows Security Settings**. Select **Next**.

10. In the **Configuration settings** tab, under **Defender**, configure the following settings:
    - TamperProtection (Device): **On**

11. Under **Windows Defender Security Center**, configure the following settings:
     - Disable Account Protection UI: **Enable**
     - Disable App Browser UI: **Enable**
     - Disable Device Security UI: **Enable**
     - Disable Family UI: **Enable**
     - Disable Health UI: **Enable**
     - Enable Customized Toasts: **Enable**

12. Next to **Company Name**, select the switch to change it to **Configured**, and then type **Contoso IT** in the text box.

13. Next to **Phone**, select the switch to change it to **Configured**, then type **555-1234** in the text box and then select **Next**.

14. In the **Scope tags** tab, select **Next**.

15. In the **Assignments** tab, type **Contoso** in the search box and choose the **Contoso Developer Devices** group, and then select **Next**.

16. In the **Review + create** tab, review the information and select **Save**.

### Task 2: Configure Microsoft Defender Antivirus policy in Intune

1. On the **Endpoint security |Antivirus** blade, select **Create Policy**.

2. In the **Create a profile** blade, for **Platform**, select **Windows**. 

3. In the **Profile** list, select **Microsoft Defender Antivirus**, then select **Create**.

4. On the **Create Policy** page, in the **Basics** tab, in the **Name** field, enter **Microsoft Defender Antivirus Settings** and then select **Next**.

5. In the **Configuration settings** tab, configure the following settings:

   - Allow scanning of all downloaded files and attachments: **Allowed (Default)**
   - Allow Realtime Monitoring: **Allowed**
   - Check For Signatures Before Running Scan: **Enabled**
   - Days to Retain Cleaned Malware: Select the switch and type **60** in the text box
   - Schedule Quick Scan Time: Select the switch and type **60** (represents 1:00AM)
   - Submit samples consent: **Send safe samples automatically**

6. In the **Configuration settings** tab, select **Next** twice.

7. In the **Assignments** tab, type **Contoso** and then select the **Contoso Developer Devices** group, and then select **Next**.

9. In the **Review + create** tab, review the information and select **Save**.

### Task 3: Sync the managed devices

1. In the Microsoft Intune admin center, select **Devices** and then select **All devices**.  

2. On the **Devices | All devices** page, select **SEA-WS2** and then on the **SEA-WS2** page, select **Sync** on the toolbar, and then select **Yes**. 

   > Wait for 3-4 minutes for the sync to complete.

3. Close Microsoft Edge.

### Task 4: Verify the configuration

1. Switch to **SEA-CL1**.

2. If necessary, sign in as **Contoso\Administrator** with the password of **Pa55w.rd**.

3. On **SEA-CL1**, select **Start**, type **Windows Security**, and then under the Windows Security icon select **Open**.

   > Notice that all security options are displayed. This is because SEA-CL1 is not enrolled to Intune.

4. Close **Windows Security** and sign out of SEA-CL1.

5. Switch to **SEA-WS2**, and if necessary, sign in as Contoso\Administrator with the password of Pa55w.rd.

6. Select **Start**, type **Windows Security**, and then under the Windows Security icon select **Open**.

   > Notice that all of the restricted areas as configured in the Intune policy are not displayed. SEA-WS2 is enrolled in Intune, which has applied the security settings.

7. Close **Windows Security** and sign out of **SEA-WS2**.

**Results**: After completing this exercise, you will have successfully created and applied a policy to configure Microsoft Defender for managed devices in Intune.

**END OF LAB**
