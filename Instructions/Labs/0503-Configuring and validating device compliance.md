# Practice Lab 0503: Configuring and validating device compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Entra Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Configuring compliance policies 

### Scenario

Contoso would like to ensure that Windows devices that are enrolled in Intune meet a minimum configuration specification. The following are specifications are required:

- Minimum Windows operating system version: 10.0.19041.329
- Microsoft Defender Antimalware required

If a device meets these requirements, it will be marked as compliant. If the device does not meet these requirements, the device should be marked as non-compliant.

### Task 1: Create and assign a compliance policy

1. Sign in to **SEA-SVR1** as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Compliance**.

6. On the **Devices | Compliance** blade, in the details pane select **+ Create policy**.

7. On the **Create a policy** blade, provide the following value and select **Create**:

    - Platform: **Windows 10 and later**
    - Profile type: **Windows 10/11 compliance policy**

8. On the **Basics** tab, provide the following value and select **Next**:

    - Name: **Compliance1**

9. On the **Compliance settings** tab, expand **Device Health** and review the available settings.

10. On the **Compliance settings** tab, expand **Device Properties**. In the **Minimum OS version**
    field, type **10.0.19041.329**.

11. On the **Compliance settings** tab, expand **System Security**. Set the **Microsoft Defender Antimalware** setting to **Require**. 

12. Select **Next**. On the **Actions for noncompliance** tab, note the action to **Mark device noncompliant** default setting is **immediately**. 

    > Review how you can configure the number of days after which the device is marked as noncompliant, and configuration additional actions. 

13. Select **Next**. On the **Assignments** tab, under **Included groups** select **Add groups**. Select **Windows Devices**, choose **Select**, and then select **Next**. 

    _Note: The **Windows Devices** group was created in Lab 0301: Creating and Deploying Configuration Profiles._

14. On the **Review + create** tab, review the settings and then select **Create**.

15. In the navigation menu, select **Devices** and then in the Devices navigation pane, select **Compliance**.

16. On the **Devices | Compliance** blade, select the **Compliance settings** tab.

17. On the **Compliance settings** page, ensure **30** is visible in the **Compliance status validity period**. If it is not, enter that value.

18. On the **Compliance settings** page, toggle **Mark devices with no compliance policy assigned as** so it reads **Not compliant** and then select **Save**. 

    > This setting will ensure that any device that does not have a compliance policy assigned will be set to **Not compliant**.

**Results**: After completing this exercise, you will have successfully configured a compliance policy.


## Exercise 2: Creating a conditional access policy to enforce compliance

### Scenario 

When a user uses a device that is marked as non-compliant, they should not be able to access their e-mail. You've been asked to configure a conditional access policy that enforces this rule, and verify it functions as expected. In some cases, the user may experience a loop where they are prompted to sign in repeatedly.

### Task 1: Create a conditional access policy

1. On **SEA-SVR1**, in the **Intune admin center** select **Devices**, then select **Conditional access**.

2. On the **Conditional Access | Overview** blade, select **Policies**.

3. On the **Conditional Access | Policies** blade, select **New policy**.

4. On the **New** blade, in the **Name** text box, type **Conditional1** and then select **0 users and groups selected**.

5. Under **Include**, select the **All users** radio button.

6. In the **Target resources** section, select **No target resources selected**.

7. Under **Include** choose the **Select resources** radio button, under the Select heading, select **None**, select **Office 365 Exchange Online**, and then click **Select**.

8. In the **Conditions** section, select **0 conditions selected**. 

9. In the list of conditions, under **Device platforms**, select **Not configured**. In the **Configure** section select **Yes**, select the **Select device platforms** radio button, select the **Windows** check box, and then select **Done**.

10. In the **Grant** section, select **0 controls selected**. Select the **Require device to be marked as compliant** check box, and then select **Select**.

11. On the **New** blade, select **On** for the **Enable policy** option and then select **Create**.

12. Close Microsoft Edge.

### Task 2: Verify that the conditional access policy is working

1. Switch to **SEA-WS3** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On **SEA-WS3**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **outlook.office.com** and then press Enter.

4. On the pick an account dialog box, select **`Aaron@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter **Pa55w.rd1234!** and select **Sign in**.

    > **Note** If the Microsoft Edge Save password prompt appears, select **Update**.

6. You should receive a message that asks you to switch Edge profile. Select **Switch Edge profile**.

7. You will be prompted with a message stating, "**Continue with your work or school account**". Select **Sign in to sync data**.

8. You will be required to enter your password again. Enter **Pa55w.rd1234!** and select **Sign in**.

9. A dialog box will appear asking, "**Automatically sign in to all desktops apps and websites on this device?**". Select **No, sign in to this app only**.

    > Note: A dialog will appear stating, "**Let's set up your profile to access org resources**". This is because SEA-WS3 is not joined to Entra ID and not managed by Intune. As such, you are unable to access Aarons' mailbox from this device.

10. **Close** all windows and sign out of **SEA-WS3**.

11. Switch to **SEA-WS1**, and sign in as as Aaron Nicholls with the PIN **102938**. 

    > Note: SEA-WS1 is a managed Windows 11 device that is enrolled in Intune.

12. On the taskbar, select **Microsoft Edge**.

13. In Microsoft Edge, type **outlook.office.com** and then press Enter. 

14. Verify that you can access Aaron's mailbox. 

    > Note: This is because SEA-WS1 is a managed device and marked as compliant.

15. Close Microsoft Edge and sign out of SEA-WS1.

### Task 3: Disable the conditional access policy

1. Switch to **SEA-SVR1** and enter the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then 
   press **Enter**.

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **All devices**.

   > Notice that SEA-WS1 is compliant, which is why Aaron was allowed to access his mailbox.

6. From the navigation pane select **Devices**, then select **Conditional access**.

7. On the **Conditional Access** page, select **Policies** and then select **Conditional1**.

8. On the **Conditional1** page, at the bottom of the page, select **Off** and then select **Save**.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured a conditional access policy to determine device compliance.

**END OF LAB**
