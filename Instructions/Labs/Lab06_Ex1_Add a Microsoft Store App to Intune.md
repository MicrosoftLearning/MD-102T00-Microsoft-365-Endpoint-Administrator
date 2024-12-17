# Practice Lab06: Manage Windows Apps

## Summary

In this lab, you create and deploy cloud-based apps using Intune and the Company Portal Website.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Add a Microsoft Store App to Intune

### Scenario

You use Microsoft Intune to manage desktops and apps for Contoso Corporation. The Research department often connects to various servers to perform tasks and has asked for the Microsoft Remote Desktop app to be available for Research members to install as needed. The Microsoft Remote Desktop is available from the Microsoft Store, but you decide to add the app to Intune so that users can access it from the Company Portal website. A Research member named Aaron Nicholls has agreed to test the installation process after you have published the app to the portal.

### Task 1: Add Microsoft Remote Desktop to Intune

1. On **MD102-WS1**, if necessary, sign in as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. Select **Devices**.
   
6. On the Devices pane, under the **Device onboarding** section, select **Enrollment**.

7. In the Enroll devices pane, ensure **Windows** is selected.

8. In the **Enrollment options** section, select **Automatic Enrollment**.

9.  On the **MDM user scope** row, select **All** and then select **Save**.

10. On the **Microsoft Intune admin center** page, select **Apps**.

11. On the **Apps** page, in the navigation pane, select **All apps**.

12. In the details pane, select **Add**.

13. On the **Select app type** page, click the drop-down menu and then Choose **Microsoft store app (new)**. Click **Select**.

14. On the **Add App** page, click **Search the  Microsoft Store app (new)**, search for and select **Microsoft Remote Desktop**. Click **Select**.

15. On the **App information** page, verify the following information and then select **Next**:
    - Name: **Microsoft Remote Desktop**
    - Publisher: **Microsoft Corporation**
    - Category: **Business**
    - Show this as a featured app in the Company Portal: **Yes**

16. Select **Next** twice and then select **Create**.

17. The Microsoft Remote Desktop page opens.

    > Take note of the Properties, Device install status, and User install status nodes.

### Task 2: Enroll Device and Perform an Entra Join

1. Switch to **MD102-WS8** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar, select **Start** and then select **Settings**.

3. In the **Settings** window, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Entra ID**.

7. On the **Sign in** page, type **MeganB@yourtenant.onmicrosoft.com** and then select **Next**.

8. On the **Enter password** page, enter the tenant password provided by your instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, select **Done**.

11. On the **Access work or school** page, verify that **Connected to Contoso's Azure AD** is displayed.

12. Close the **Settings** page.

13. Sign out the **Admin** user.

### Task 3: Assign a Group to the App

1. Switch to **MD102-WS1**.

2. In the Microsoft Remote Desktop page, select **Properties**.

3. In the details pane, scroll down to the **Assignments** section and then select **Edit**.

4. On the **Assignments** page, select **Add group** in the **Available for enrolled devices**.

5. On the **Select groups** page, MD102rch and select the **Contoso** group and then click **Select**.

6. Select **Review + save** and then select **Create**.

### Task 4: Force policy synchronization from the Intune console

1. In the **Microsoft Intune admin center**, select **Devices** and then select **All devices**.

2. In the details pane, select **MD102-WS8**.

3. On the **MD102-WS8** blade, select **Sync** and when prompted select **Yes**.

   > Intune will contact the device and tell it to synchronize all policies. This may take up to 5 minutes.


### Task 5: Install an app from the Company Portal Website

1. Switch to **MD102-WS8** and sign in with **Megan Bowen**.

2. At the **Use Windows Hello with your account** page, select **OK**.

3. On the **More information required** page, select **Next**.

4. On the **Keep your account secure** page, select **Next**.

5. Select **Next**, scan the QR code and **finish** the Authenticator setup.

6. On the verification page, select **Next** and then select **Done**.

7. On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **`102938`** and then select **OK**.

8. On the **All set!** page, select **OK**.

9.  On the taskbar, select **Microsoft Edge**.

10. If necessary, at the **Welcome to Microsoft Edge** page, select **Confirm and continue**. Close the Welcome page.

11. In the address bar browse to **https://portal.manage.microsoft.com** and then press **Enter**.

12. Sign in as **Megan Bowen**.

13. On the Contoso web portal, select **Devices**.

14. On the Devices page, select **Tap here to tell us which device you're using or add a new device**.

15. On the **Which device are you using** dialog box, select the option next to **MD102-WS8**, and then select **Select**.

   > Notice that the message now changes to Apps will be installed onto: MD102-WS8

16. At the top-left corner, select the navigation button and then select **Apps**.

   > Take note of the Microsoft Remote Desktop app listed on the Apps page. **Note** It might take a few minutes for the app to appear.

17. Select **Microsoft Remote Desktop**.

18. On the Microsoft Remote Desktop page, select **Install**.

19. If prompted, on the **Install Microsoft Remote Desktop** dialog box, select **Always allow portal.manage.microsoft.com to open links of this type in the associated app** and then select **Open**.

   >It may take a few minutes for the app to install.

20. After the app is installed close all open windows.

21. Select **Start** and verify that **Remote Desktop** is displayed on the Start menu.

**Results**: After completing this exercise, you will have successfully added and installed a Microsoft Store App from Intune.

**END OF LAB**