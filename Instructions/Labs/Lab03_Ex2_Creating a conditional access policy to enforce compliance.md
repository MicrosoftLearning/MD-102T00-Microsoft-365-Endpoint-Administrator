# Practice Lab03: Manage Windows Device Compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 2: Creating a conditional access policy to enforce compliance

### Scenario 

When a user uses a device that is marked as non-compliant, they should not be able to access their e-mail. You've been asked to configure a conditional access policy that enforces this rule, and verify it functions as expected. In some cases, the user may experience a loop where they are prompted to sign in repeatedly.

### Task 1: Enable Windows Automatic Enrollment into Microsoft Intune

1. In **MD102-WS1**, open a new tab in **Microsoft Edge**, and then in the address bar type **https://intune.microsoft.com**, and then press **Enter**. 

   > The Microsoft Intune admin center opens.

2. In the Microsoft Intune admin center, select **Devices**.

3. On the Devices pane, under the **Device onboarding** section, select **Enrollment**.

4. In the Enroll devices pane, ensure **Windows** is selected.

5. In the **Enrollment options** section, select **Automatic Enrollment**.

6. On the **MDM user scope** row, select **All** and then select **Save**.

   _**Note**: By performing this step, you enabled automatic enrollment into Intune for any User that performs an Entra join or Entra registration from a Windows device._

### Task 2: Automatically enroll a Windows device to Microsoft Intune

1. Sign in to **MD102-WS5** as **Admin** with the password of **Pa55w.rd**.

2. Select **Start** and then select **Settings**.

3. In **Settings**, select **Accounts**.

4. On the Accounts page, select **Access work or school**.

5. In the **Access work or school** page, select **Connect**.

6. In the **Microsoft account** window, select **Join this device to Microsoft Entra ID**.

7. On the **Sign in** page, type **`LynneR@yourtenant.onmicrosoft.com`** and then select **Next**.

8. On the **Enter password** page, enter the user password provided by your lab instructor and then select **Sign in**.

9. On the **Make sure this is your organization** dialog box, select **Join**.

10. On the **You're all set!** page, read the information and then select **Done**.

11. In the **Access work or school** section, verify that **Connected to Contoso's Azure AD** displays.

12. Select **Connected to Contoso's Azure AD** and then select **Info**.

13. Take note of the information regarding the areas managed by Contoso, scroll down, and then select **Sync**. This will force a Device sync with Intune.

14. Close the **Settings** window.

### Task 3: Sign in as an Entra user

1. Sign out of **MD102-WS5**.

2. Select **Other user**, and sign in as **`LynneR@yourtenant.onmicrosoft.com`** with the user password provided by your lab instroctur. Wait for the profile to be created.

3. At the **Use Windows Hello with your account** page, select **OK**.

4. On the **More information required** page, select **Next**.

5. On the **Keep your account secure** page, select **Next**.

6. Select **Next**, scan the QR code and **finish** the Authenticator setup.

7. On the verification page, select **Next** and then select **Done**.

8.  On the **Set up a PIN** page, in the **New PIN** and **Confirm PIN** boxes, type **102938** and then select **OK**.

9. On the **All set!** page, select **OK**.

### Task 3: Create a conditional access policy

1. Switch to **MD102-WS1** and if necessary, sign in as **Admin** with the password of **Pa55w.rd**.

2. On the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. in the **Intune admin center** select **Devices**, then select **Conditional access**.

5. On the **Conditional Access | Overview** page, select **Policies**.

6. On the **Conditional Access | Policies** page, select **New policy**.

7. On the **New** blade, in the **Name** text box, type **Conditional1** and then select **0 users and groups selected**.

8. Under **Include**, select the **All users** radio button.

9. In the **Target resources** section, select **No target resources selected**.

10. Under **Include** choose the **Select resources** radio button, under the Select heading, select **None**, select **Office 365 Exchange Online**, and then select **Select**.

11. In the **Conditions** section, select **0 conditions selected**. 

12. In the list of conditions, under **Device platforms**, select **Not configured**. 

13. On the **Device plarforms** blade, in the **Configure** section select **Yes**, then select the **Select device platforms** radio button, select the **Windows** check box, and then select **Done**.

14. In the **Grant** section, select **0 controls selected**, then select the **Require device to be marked as compliant** check box, and then select **Select**.

15. On the **New** blade, select **On** for the **Enable policy** option and then select **Create**.

16. Close Microsoft Edge.

### Task 4: Verify that the conditional access policy is working

1. Sign-in to **MD102-WS6** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On **MD102-WS6**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **outlook.office.com** and then press Enter.

4. On the pick an account dialog box, select **`LynneR@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the user password provided by your lab instructor and select **Sign in**. If the Microsoft Edge Save password prompt appears, select **Got it**.

6. You should receive a message that ask you to switch Edge profile. Select **Switch Edge profile**.

7. You will be prompted with a message stating, "**Continue with your work or school account**". Select Sign in to sync data.

8. You will be required to enter your password again. Enter the user password provided by your lab instructor and select **Sign in**.

9. A message will appear stating, "**Stay signed in to all your apps**". Select **no, sign in to this app only**.

    > Note: A prompt will appear stating, "**Allow my organization to manage my device**". This is because MD102-WS6 is not joined to Entra ID and not managed by Intune. As such, you are unable to access Aarons' mailbox from this device.

10. **Close** all windows and sign out of **MD102-WS6**.

11. Switch to **MD102-WS5**, and sign in as as Lynee Robbins with the PIN **102938**. 

    > Note: MD102-WS5 is a managed Windows 11 device that is enrolled in Intune.

12. On the taskbar, select **Microsoft Edge**.

13. In Microsoft Edge, type **outlook.office.com** and then press Enter. 

14. Verify that you can access Aaron's mailbox. 

    > Note: This is because MD102-WS5 is a managed device and marked as compliant._

15. Close Microsoft Edge and sign out of MD102-WS5.

### Task 3: Disable the conditional access policy

1. Switch to **MD102-WS1** and enter the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then 
   press **Enter**.

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **All devices**.

   > Notice that MD102-WS1 is compliant, which is why Aaron was allowed to access his mailbox.

6. From the navigation pane select **Devices**, then select **Conditional access**.

7. On the **Conditional Access** page, select **Policies** and then select **Conditional1**.

8. On the **Conditional1** page, at the bottom of the page, select **Off** and then select **Save**.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured a conditional access policy to determine device compliance.

**END OF LAB**
