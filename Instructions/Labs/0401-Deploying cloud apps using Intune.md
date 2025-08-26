# Practice Lab 0401: Deploying cloud apps using Intune

## Summary

In this lab, you create and deploy cloud-based apps using Intune and the Company Portal Website.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Entra Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Add a Microsoft Store App to Intune

### Scenario

You use Microsoft Intune to manage desktops and apps for Contoso Corporation. The Research department often connects to various servers to perform tasks and has asked for the Windows App to be available for Research members to install as needed. The Windows App is available from the Microsoft Store, but you decide to add the app to Intune so that users can access it from the Company Portal website. A Research member named Aaron Nicholls has agreed to test the installation process after you have published the app to the portal.

### Task 1: Add Windows App to Intune

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. On the **Microsoft Intune admin center** page, select **Apps**.

6. On the **Apps** page, in the navigation pane, select **All apps**.

7. In the details pane, select **+ Create**.

8. On the **Select app type** page, click the drop-down menu and then Choose **Microsoft store app (new)**. Click **Select**.

9. On the **Add App** page, click **Seach the  Microsoft Store app (new)**, search for and select **Windows App**. Click **Select**.

10. On the **App information** page, verify the following information and then select **Next**:
    - Name: **Windows App**
    - Publisher: **Microsoft Corp.**
    - Category: **Business**
    - Show this as a featured app in the Company Portal: **Yes**

11. Select **Next** twice and then select **Create**.

12. The Windows App page opens.

    > Take note of the Properties, Device install status, and User install status nodes.

### Task 2: Assign a Group to the App

1. In the **Windows App** page, under **Manage**,  select **Properties**.

2. In the details pane, scroll down to the **Assignments** section and then select **Edit**.

3. On the **Assignments** page, select **Add group** in the **Available for enrolled devices**.

4. On the **Select groups** page, search and select the **Research** group and then click **Select**.

5. Select **Review + save** and then select **Save**.

### Task 3: Force policy synchronization from the Intune console

1. In the **Microsoft Intune admin center**, select **Devices** and then select **All devices**.

2. In the details pane, select **SEA-WS1**.

3. On the **SEA-WS1** blade, select **Sync** and when prompted select **Yes**.

   > Intune will contact the device and tell it to synchronize all policies. This may take up to 5 minutes.


### Task 4: Install an app from the Company Portal Website

1. Switch to **SEA-WS1**.

2. Sign in as **Aaron Nicholls** with the PIN **102938**.

3. On the taskbar, select **Microsoft Edge**.

4. If necessary, at the **Welcome to Microsoft Edge** page, select **Confirm and continue**. Close the Welcome page.

5. In the address bar browse to **https://portal.manage.microsoft.com** and then press **Enter**.

6. Sign in as **Aaron Nicholls**.

7. On the Contoso web portal, select **View Devices**.

8. On the Devices page, select **Tap here to tell us which device you're using or add a new device**.

9. On the **Which device are you using** dialog box, select the option next to **SEA-WS1**, and then select **Select**.

   > Notice that the message now changes to Apps will be installed onto: SEA-WS1

10. At the top-left corner, select the navigation button and then select **Apps**.

   > Take note of the Windows app listed on the Apps page. **Note** It might take a few minutes for the app to appear.

11. Select **Windows App**.

12. On the Windows App page, select **Install**.

13. If prompted, on the **Install Windows App** dialog box, select **Always allow portal.manage.microsoft.com to open links of this type in the associated app** and then select **Open**.

   >It may take a few minutes for the app to install.

14. After the app is installed close all open windows.

15. Select **Start** and verify that **Windows App** is displayed on the Start menu.

**Results**: After completing this exercise, you will have successfully added and installed a Microsoft Store App from Intune.

## Exercise 2: Configure and deploy Microsoft 365 Apps from Intune

### Scenario

All the users of the Research department at Contoso require Microsoft 365 Apps. You've been asked to deploy the 64-bit versions of Microsoft Excel, Outlook, PowerPoint and Word to their Windows devices. You also need to ensure they are configured for the Current Channel for updates.

### Task 1: Verify installed apps on SEA-WS1

1. On **SEA-WS1**, on the taskbar, select **Start** and then select the **Settings** app.

2. In the **Settings** app, select **Apps**, and then select **Apps & features**.

   > Verify that **Microsoft 365 Apps for enterprise - en-us** is not listed.

3. Close all open windows.

### Task 2: Add Microsoft 365 apps to Intune

1. On **SEA-SVR1**, in the **Microsoft Intune admin center**, select **Apps**.

2. In the **Apps | Overview** blade, select **All Apps**. In the details pane, select **Create**.

3. In the **Select app type** blade, under **Microsoft 365 Apps**, select **Windows 10 and later** , and then click **Select**.

4. On the **Add Microsoft 365 Apps** blade, configure the following options and select **Next**:

    - Suite Name: **Microsoft 365 Apps (Research)**

    - Description: **Microsoft 365 Apps for the Research dept at Contoso**

5. On the **Configure app suite** tab, expand the **Select Office apps** dropdown, and ensure that only the following apps are selected:

    - Excel

    - Outlook

    - PowerPoint

    - Word

6. On the **App suite information** section, configure the following options:

     - Architecture: **64-bit**

     - Default file format: **Office Open XML Format**

     - Update channel: **Monthly Enterprise Channel**

7. On the **Properties** section, configure the following options and select **Next**:

     - Accept the Microsoft Software License Terms on behalf of users: **Yes**
     
8. On the **Assignments** tab, in the **Required** section, select **Add group**.

9. On the **Select groups** blade, select **Research**, and then choose **Select**.

10. Select **Next**. On the **Review + Create** tab, select **Create**.

11. On the **Microsoft 365 Apps (Research)** page, select **Properties**.

12. In the details pane verify that **Research** is listed under **Required** in the **Assignments** section.

### Task 3: Request policy synchronization from the Intune console

1. In the **Microsoft Intune admin center**, select **Devices** and then select **All devices**.

2. In the details pane, select **SEA-WS1**.

3. On the **SEA-WS1** blade, select **Sync** and when prompted select **Yes**.

   > Intune will contact the device and tell it to synchronize all policies. This may take up to 15 minutes. You may choose to Sync from **SEA-WS1**

### Task 4: Verify Microsoft 365 apps are installed

1. Switch to **SEA-WS1** and wait approximately 10-15 minutes for the Microsoft 365 Suite to install on the device.

2. Sign out of **SEA-WS1** and then sign back in as **Aaron Nicholls** with the PIN **102938**.

3. On **SEA-WS1**, on the taskbar, select **Start** and then select the **Settings** app.

4. In the **Settings** app, select **Apps** and on the **Apps & features** page, scroll down and verify that **Microsoft 365 Apps for enterprise - en-us** is listed.

5. Close the **Settings** app and select the **Start** button.

6. Select all apps, scroll down to **W** and select **Word** and verify that the app opens.

   > _Note: Recall in a previous lab, you removed recently added apps from the Start Menu._

7. Close all open windows.

8. Sign out of SEA-WS1.

### Task 5: Monitor app installation status in Intune

1. Switch to **SEA-SVR1**.

2. In the **Microsoft Intune admin center**, select **Apps**.

3. On the **Apps | Overview** blade, select **Monitor** and then select **App install status**.

4. In the details pane, select **Microsoft 365 Apps \(Research\)**.

5. In the details pane, under **Monitor** and under **User install status**, verify that **1** is displayed under Installed.

   _Note: It may take some time for the information to display._
   
   _Note: This indicates that the app is installed on one device and for one user._

6. Select **Device install status**.

   > In the details pane, you can see the devices that the app is installed on, and also the name of the user. The **Device Name** column should list **SEA-WS1** and the **Status** column should say **Installed**. This means that the app is installed on SEA-WS1.

7. In the **Microsoft Intune admin center**, select **Devices**.

8. On the **Devices | Overview** blade, select **All devices** and then in the details pane, select **SEA-WS1**.

9. On the **SEA-WS1** blade, select **Managed Apps**.

10. On the **SEA-WS1 | Managed Apps** blade, in the details pane, select **Microsoft 365 Apps (Research)**.

   > On the **Microsoft 365 Apps (Research) - Installation details** window, you can see the entire lifecycle of the application, that is - when it was created, assigned, installation time and status and the last time the device checked in (synced with Intune).

11. Close all open windows.

**Results**: After completing this exercise, you will have successfully configured and deployed Microsoft 365 Apps from Intune.

**END OF LAB**
