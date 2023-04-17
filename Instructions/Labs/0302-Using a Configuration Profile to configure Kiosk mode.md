# Practice Lab: Using a Configuring Profile to configure Kiosk mode

## Summary

In this lab, you use Microsoft Intune to create and apply a Configuration profile to run single-app Kiosk mode on a Windows 11 device.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0203-Manage Device Enrollment into Intune


> Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.


## Exercise 1: Create and apply a Configuration profile

### Scenario

You have been asked to configure SEA-WS2 as a Windows 11 kiosk to allow Contoso visitors the ability to browse the Internet. You need to ensure that the kiosk is configured as follows:

-   A single app, full-screen kiosk.
-   Auto logon.
-   Provides access to the Microsoft Edge browser, which is to be configured in Public Browsing (InPrivate) mode. The home page should be configured for http://bing.com.

### Task 1: Enroll SEA-WS2 to Microsoft Intune

1. Sign in to **SEA-WS2** as **Admin** with the password of **Pa55w.rd**.

2. Select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Azure Active Directory**.

7. On the **Sign in** page, type **`AllanD@yourtenant.onmicrosoft.com`** and then select **Next**.


8. On the **Enter password** page, enter the Tenant password and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, read the information and then select **Done**.

11. In the **Access work or school** section, verify that **Connected to Contoso's Azure AD** displays.

12. Select **Connected to Contoso's Azure AD** and then select **Info**.

13. Scroll down, and then select **Sync**. This will force a Device sync with Intune.

14. Close the **Settings** window.

### Task 2: Create the Contoso Kiosk device group

1. Switch to **SEA-SVR1** and sign in as **Contoso\Administrator** with the password of **Pa55w.rd**. Close Server Manager.

2. On **SEA-SVR1**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.
5. In the Microsoft Endpoint Manager admin center, in the navigation pane, select **Groups**.

6. On the **Groups | All groups** blade, select **New group**.

7. On the **New Group** blade, enter the following information:

- Group type: **Security**
- Group name: **Contoso Kiosk Devices**
- Group description: **All Windows devices configured as a Kiosk**
- Membership type: **Assigned**

8. Under **Members**, select **No members selected**. 

9. On the **Add members** blade, in the **Search** box type **Sea**. Select **SEA-WS2** and then choose **Select**.

10. On the **New Group** blade, select **Create**. 

11. On the **Groups | All groups** blade, verify that the **Contoso Kiosk Devices** group is displayed. You may need to select the Refresh button for the new group to become visible.

### Task 3: Create a Configuration profile based on scenario requirements

1. In the Microsoft Endpoint Manager admin center, select **Devices** from the navigation bar.

2. On the **Devices | Overview** page, select **Configuration Profiles**.

3. On the **Devices | Configuration profiles** blade, in the details pane, select **Create profile**.

4. In the **Create a profile** blade, select the following options, and then select **Create**:

   - Platform: **Windows 10 and later**
   - Profile type: **Templates**
   - Template name: **Kiosk**

5. In the **Basics** blade, enter the following information, and then select **Next**:

- Name: **Contoso Kiosk Policy**
- Description: **Basic settings for Contoso Kiosk Devices.**

6. On the **Configuration settings** blade, next to **Select a kiosk mode**, select **Single app, full-screen kiosk**. 

   > Additional options display based upon the mode selected.

7. On the **Configuration settings** blade, select the following options, and then select **Next**:

   - User logon type: **Auto logon (Windows 10, version 1803 and later, or Windows 11)**
   - Application type: **Add Microsoft Edge browser**
     - Edge Kiosk URL: **http://bing.com**
     - Microsoft Edge kiosk mode type: **Public Browsing (InPrivate)**
     - Refresh browser after idle time: **5**
   - Specify Maintenance Window for App Restarts: **Not configured**

8. On the **Assignments** blade, under **Included groups**, select **Add groups**.

9. In the **Select groups to include** window, select **Contoso Kiosk Devices**, and then click **Select**.

10. Select **Next** two times until you reach the **Review + create** blade. Select **Create**.

11. Close Microsoft Edge.

### Task 4: Verify that the Configuration profile is applied

1. Switch to **SEA-WS2**.

2. On **SEA-WS2**, on the taskbar, select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts** and then select **Access work or school**.

4. In the **Access work or school** section, select the **Connected to Contoso's Azure AD** link and then select **Info**.

5. In the **Managed by Contoso** page, scroll down and then under Device sync status, select **Sync**. Wait for the synchronization to complete. 

6. Close the **Settings** app.

7. Restart **SEA-WS2**.

   > Notice that SEA-WS2 automatically sign in and creates a profile. After the sign-in is complete, Microsoft Edge is displayed configured with inPrivate browsing. If SEA-WS2 does not sign in automatically, repeat steps 1-7 to ensure that the policy has refreshed on the device.

**Results**: After completing this exercise, you will have successfully created and assigned a Configuration profile to configure a Windows 11 device as a single-app kiosk.

**END OF LAB**
