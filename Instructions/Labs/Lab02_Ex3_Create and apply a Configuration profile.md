# Practice Lab02: Manage Windows Device Configuration

## Summary

In this lab, you use Microsoft Intune to create and apply a Configuration profile to run single-app Kiosk mode on a Windows 11 device.

## Exercise 3: Create and apply a Configuration profile

### Scenario

You have been asked to configure SEA-WS3 as a Windows 11 kiosk to allow Contoso visitors the ability to browse the Internet. You need to ensure that the kiosk is configured as follows:

-   A single app, full-screen kiosk.
-   Auto logon.
-   Provides access to the Microsoft Edge browser, which is to be configured in Public Browsing (InPrivate) mode. The home page should be configured for https://bing.com.

### Task 1: Enroll SEA-WS3 to Microsoft Intune

1. On the **SEA-WS3** taskbar, select **Start** and then select **Settings**.

1. Select **Start** and then select **Settings**.

1. In **Settings**, select **Accounts**.

1. On the Accounts page, select **Access work or school**.

1. In the **Access work or school** page, select **Enroll only in device management**.

1. In the **Microsoft account** window, type **`AllanD@yourtenant.onmicrosoft.com`** and then select **Next**.

1. On the **Enter password** page, enter your user password provided by your instructor and then select **Sign in**.

1. On the **Stay signed in?** page, select **No**.

1. On the **Setting up your device** page, select **Got it**. 

1. Close the **Settings** window.

### Task 2: Create the Contoso Kiosk device group

1. Switch to **SEA-WS1** and sign in as **Contoso\Administrator** with the password of **Pa55w.rd**. Close Server Manager.

2. On **SEA-WS1**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. In the Microsoft Intune admin center, in the navigation pane, select **Groups**.

6. On the **Groups | Overview** page, select **New group**.

7. On the **New Group** blade, enter the following information:

   - Group type: **Security**
   - Group name: **Contoso Kiosk Devices**
   - Group description: **All Windows devices configured as a Kiosk**
   - Membership type: **Assigned**

8. Under **Members**, select **No members selected**. 

9. On the **Add members** blade, in the **Search** box type **SEA-WS3**, then select **SEA-WS3** and then select **Select**.

10. On the **New Group** pblade, select **Create**. 

11. On the **Groups | overview** page, select **All groups** and verify that the **Contoso Kiosk Devices** group is displayed. You may need to select the Refresh button for the new group to become visible.

### Task 3: Create a Configuration profile based on scenario requirements

1. In the Microsoft Intune admin center, select **Devices** from the navigation bar.

2. On the **Devices | Overview** page, select **Configuration**.

3. On the **Devices | Configuration** page, in the **Policies** tab, select **+ Create**, and then select **+ New Policy**.

4. In the **Create a profile** blade, select the following options, and then select **Create**:

   - Platform: **Windows 10 and later**
   - Profile type: **Templates**
   - Template name: **Kiosk**

5. In the **Basics** blade, enter the following information, and then select **Next**:

   - Name: **Contoso Kiosk Policy**
   - Description: **Basic settings for Contoso Kiosk Devices.**

6. In the **Configuration settings** tab, next to **Select a kiosk mode**, select **Single app, full-screen kiosk**. 

   > Additional options display based upon the mode selected.

7. In the **Configuration settings** tab, select the following options, and then select **Next**:

   - User logon type: **Auto logon (Windows 10, version 1803 and later, or Windows 11)**
   - Application type: **Add Microsoft Edge browser**
     - Edge Kiosk URL: **https://bing.com**
     - Microsoft Edge kiosk mode type: **Public Browsing (InPrivate)**
     - Refresh browser after idle time: **5**
   - Specify Maintenance Window for App Restarts: **Not configured**

8. On the **Assignments** blade, under **Included groups**, select **Add groups**.

9. In the **Select groups to include** window, select **Contoso Kiosk Devices**, and then select **Select**.

10. Select **Next** two times until you reach the **Review + create** tab, and then select **Create**.

11. Close Microsoft Edge.

### Task 4: Verify that the Configuration profile is applied

1. Switch to **SEA-WS3**.

2. On **SEA-WS2**, on the taskbar, select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts** and then select **Access work or school**.

4. In the **Access work or school** section, select the **Connected to Contoso MDM** link and then select **Info**.

5. In the **Managed by Contoso** page, scroll down and then under Device sync status, select **Sync**. Wait for the synchronization to complete. 

6. Close the **Settings** app.

7. Restart **SEA-WS3**.

   > Notice that SEA-WS3 automatically signs in and creates a profile. After the sign-in is complete, Microsoft Edge is displayed configured with InPrivate browsing. If SEA-WS2 does not sign in automatically, repeat steps 1-7 to ensure that the policy has refreshed on the device.

**Results**: After completing this exercise, you will have successfully created and assigned a Configuration profile to configure a Windows 11 device as a single-app kiosk.

**END OF LAB**
