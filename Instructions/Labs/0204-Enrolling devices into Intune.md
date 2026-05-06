---
lab:
  title: 'Practice Lab 0204: Enrolling devices into Microsoft Intune'
  description: In this lab, you will join a Windows client to Entra ID and verify that the device has automatically enrolled into Microsoft Intune.
  duration: 108 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Windows
---

# Practice Lab 0204: Enrolling devices into Microsoft Intune

## Summary

In this lab, you will join a Windows client to Microsoft Entra ID and verify that the device has automatically enrolled into Microsoft Intune.

### Prerequisites

The following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Microsoft Entra Connect

- 0203-Manage Device Enrollment into Intune

> [!NOTE]
> You will also need a mobile phone that can receive text messages used to secure Windows Hello sign-in authentication to Microsoft Entra ID.

### Scenario

You have assigned Aaron Nicholls appropriate licenses and will now test the process of joining a Windows device to Microsoft Entra ID and have it automatically enroll in Microsoft Intune.

### Task 1: Automatically enroll a Windows device to Microsoft Intune

1. Sign in to **SEA-WS1** as **Admin** with the password of **Pa55w.rd**.

2. Select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts**.

4. On the **Accounts** page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Microsoft Entra ID**.

7. On the **Sign in** page, type **`Aaron@yourtenant.onmicrosoft.com`** and then select **Next**.

8. On the **Enter password** page, enter **Pa55w.rd** and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, read the information and then select **Done**.

11. In the **Access work or school** section, verify that **Connected to Contoso's Azure AD** displays.

12. Select **Connected to Contoso's Azure AD** and then select **Info**.

13. Take note of the information regarding the areas managed by Contoso, scroll down, and then select **Sync**. This will force a Device sync with Intune.

14. Close the **Settings** window.

### Task 2: Validate device enrollment into Microsoft Entra ID and Intune

1. On the **SEA-WS1** taskbar, select **Start**, type **cert**, and select **Manage computer certificates**. At the **User Account Control** dialog, select **Yes**.
  
2. In the **Certificates** console, in the navigation pane, expand **Personal** and select the **Certificates** node. Verify that the following certificates are listed in the details pane:

   - Microsoft Intune MDM Device CA
   - MS-Organization-Access
   - MS-Organization-P2P-Access \[2026\]

   > This indicates that the device is Microsoft Entra joined and Intune enrolled.

3. Close the Certificates window.

4. Right-click **Start**, and then select **Windows Terminal**.

5. In the PowerShell console, type the following and press **Enter**: 

   ```powershell
   dsregcmd /status
   ```

6. In the output under **Device State**, verify that **AzureAdJoined : YES** is displayed. This indicates that the device is Microsoft Entra joined.

7. In the output under **Tenant Details**, verify that the following three entries exist:

   ```cmd
   mdmUrl : https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc
   mdmTouUrl : https://portal.manage.microsoft.com/TermsofUse.aspx
   mdmComplianceUrl : https://portal.manage.microsoft.com/?portalAction=Compliance
   ```

   > [!NOTE]
   > These entries indicate that the device is enrolled in Intune.

### Task 3: Sign in as a Microsoft Entra user

1. Sign out of **SEA-WS1**.

2. Select **Other user**, and sign in as **`Aaron@yourtenant.onmicrosoft.com`** with the password **Pa55w.rd**.

3. At the **Use Windows Hello with your account** page, select **OK**.

4. On the **Let's keep your account secure** page, select **Next**.

5. On the **Install Microsoft Authenticator** page, select **Set up a different way to sign in**.

   > [!NOTE]
   > Ensure you select the correct link.

6. On the **Add a sign-in method** dialog box, select **Phone**.

   > [!NOTE]
   > This lab environment does not support SMS delivery to non-US phone numbers.
   > If you do not have a US phone number, select **Set up a different way to sign in**
   > and choose **Microsoft Authenticator** to complete MFA registration.

7. On the **Add your phone number** page, select your **Country code** and in the **Phone number** field, enter your mobile phone number which is able to receive text messages, then select **Next**.

8. When you receive the verification code, enter the code on the **Verify your phone number** page and then select **Next**.

9. On the **Phone number added** page, select **Done**.

10. On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type `102938` and then select **OK**.

11. On the **All set!** page, select **OK**.

12. Sign out of **SEA-WS1**.

### Task 4: Verifying device enrollment in the Intune console

1. Switch to **SEA-SVR1** as **Contoso\Administrator** with the password of **Pa55w.rd**.

2. In Microsoft Edge, type `https://intune.microsoft.com` in the address bar, and then press **Enter**.

3. Sign in with your Tenant administrator account.

4. In the navigation pane, select **Devices**.

5. On the **Devices | Overview** blade, under **Manage devices by platform**, verify that **1** is displayed under **Windows**. It may take a while to display.

6. On the **Devices | Overview** blade, select **All devices** and verify that **SEA-WS1** is listed.

7. Note that for **SEA-WS1**, the **Managed by** column displays **Intune** and the **Ownership** column displays **Corporate**.

   > [!NOTE]
   > This view lists devices that are enrolled to Intune. Remember that you configured automatic enrollment between Microsoft Entra ID and Intune, and because of that, any device that is joined or registered to Microsoft Entra ID is automatically enrolled to Intune. Any devices joined prior to setting up enrollment are only joined or registered to Microsoft Entra ID, but not enrolled in Intune.

8. Open a new tab in **Microsoft Edge**, in the address bar type `https://entra.microsoft.com`, and then press **Enter**.

9. In the Microsoft Entra admin center, in the navigation pane, select **Devices**, then select **All devices**.

   > Take note of **SEA-WS1**. Notice that the **Join Type** column displays **Microsoft Entra joined** and the **MDM** column displays **Microsoft Intune**.

10. Close all open windows.

**Results**: After completing this exercise, you have successfully joined a Windows client to Microsoft Entra ID and verified that the device has automatically enrolled into Microsoft Intune.

**END OF LAB**
