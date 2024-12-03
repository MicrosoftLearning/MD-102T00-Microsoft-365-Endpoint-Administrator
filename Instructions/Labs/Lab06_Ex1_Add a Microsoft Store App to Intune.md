# Practice Lab06: Manage Windows Apps

## Summary

In this lab, you create and deploy cloud-based apps using Intune and the Company Portal Website.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Add a Microsoft Store App to Intune

### Scenario

You use Microsoft Intune to manage desktops and apps for Contoso Corporation. The Research department often connects to various servers to perform tasks and has asked for the Microsoft Remote Desktop app to be available for Research members to install as needed. The Microsoft Remote Desktop is available from the Microsoft Store, but you decide to add the app to Intune so that users can access it from the Company Portal website. A Research member named Aaron Nicholls has agreed to test the installation process after you have published the app to the portal.

### Task 1: Add Microsoft Remote Desktop to Intune

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. On the **Microsoft Intune admin center** page, select **Apps**.

6. On the **Apps** page, in the navigation pane, select **All apps**.

7. In the details pane, select **Add**.

8. On the **Select app type** page, click the drop-down menu and then Choose **Microsoft store app (new)**. Click **Select**.

9. On the **Add App** page, click **Seach the  Microsoft Store app (new)**, search for and select **Microsoft Remote Desktop**. Click **Select**.

10. On the **App information** page, verify the following information and then select **Next**:
    - Name: **Microsoft Remote Desktop**
    - Publisher: **Microsoft Corporation**
    - Category: **Business**
    - Show this as a featured app in the Company Portal: **Yes**

11. Select **Next** twice and then select **Create**.

12. The Microsoft Remote Desktop page opens.

    > Take note of the Properties, Device install status, and User install status nodes.

### Task 2: Assign a Group to the App

1. In the Microsoft Remote Desktop page, select **Properties**.

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

7. On the Contoso web portal, select **Devices**.

8. On the Devices page, select **Tap here to tell us which device you're using or add a new device**.

9. On the **Which device are you using** dialog box, select the option next to **SEA-WS1**, and then select **Select**.

   > Notice that the message now changes to Apps will be installed onto: SEA-WS1

10. At the top-left corner, select the navigation button and then select **Apps**.

   > Take note of the Microsoft Remote Desktop app listed on the Apps page. **Note** It might take a few minutes for the app to appear.

11. Select **Microsoft Remote Desktop**.

12. On the Microsoft Remote Desktop page, select **Install**.

13. If prompted, on the **Install Microsoft Remote Desktop** dialog box, select **Always allow portal.manage.microsoft.com to open links of this type in the associated app** and then select **Open**.

   >It may take a few minutes for the app to install.

14. After the app is installed close all open windows.

15. Select **Start** and verify that **Remote Desktop** is displayed on the Start menu.

**Results**: After completing this exercise, you will have successfully added and installed a Microsoft Store App from Intune.

**END OF LAB**