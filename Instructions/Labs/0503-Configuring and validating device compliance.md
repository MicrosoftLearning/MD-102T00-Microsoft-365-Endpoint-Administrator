# Practice Lab: Configuring and validating device compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Azure AD

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

## Exercise 1: Configuring compliance policies 

### Scenario

Contoso would like to ensure that Windows devices that are enrolled in Intune meet a minimum configuration specification. The following are specifications are required:

- Minimum Windows operating system version: 10.0.19041.329
- Microsoft Defender Antimalware required

If a device meets these requirements, it will be marked as compliant. If the device does not meet these requirements, the device should be marked as non-compliant.

### Task 1: Create and assign a compliance policy

1. Sign in to **SEA-SVR1** as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Compliance policies**.

6. On the **Compliance policies | Policies** blade, in the details pane select **Create Policy**.

7. On the **Create a policy** blade, provide the following value and select **Create**:

- Platform: **Windows 10 and later**

8. On the **Basics** tab, provide the following value and select **Next**:

- Name: **Compliance1**

9. On the **Compliance settings** tab, expand **Device Health** and review the available settings.

10. On the **Compliance settings** tab, expand **Device Properties**. In the **Minimum OS version**
    field, type **10.0.19041.329**.

11. On the **Compliance settings** tab, expand **System Security**. Set the **Microsoft Defender Antimalware** setting to **Require**. 

12. Select **Next**. On the **Actions for noncompliance** tab, note the action to **Mark device noncompliant** default setting is **immediately**. 

    > Review how you can configure the number of days after which the device is marked as noncompliant, and configuration additional actions. 

13. Select **Next**. On the **Assignments** tab, select **Add groups**. Select **Windows Devices**, choose **Select**, and then select **Next**. 

    _Note: The **Windows Devices** group was created in the Module 0301 lab._

14. Select **Create**.

15. In the navigation menu, select **Devices** and then in the Devices navigation pane, select **Compliance policies**.

16. On the **Compliance policies** page, select **Compliance policy settings**.

17. On the **Compliance policy settings** page, next to **Mark devices with no compliance policy assigned as**, select **Not Compliant** and then select **Save**. 

    > This setting will ensure that any device that does not have a compliance policy assigned will be set to **Not compliant**.

**Results**: After completing this exercise, you will have successfully configured a compliance policy.


## Exercise 2: Creating a conditional access policy to enforce compliance

### Scenario 

When a user uses a device that is marked as non-compliant, they should not be able to access their e-mail. You've been asked to configure a conditional access policy that enforces this rule, and verify it functions as expected.

### Task 1: Create a conditional access policy

1. On **SEA-SVR1**, in the **Microsoft Endpoint Manager admin center** select **Devices**, then select **Conditional access**.

2. In the **Details** pane, select **New policy**.

3. On the **New** blade, in the **Name** text box, type **Conditional1** and then select **0 users or workload identities selected**.

4. On the **Users and groups** blade, select the **All users** radio button.

5. On the **New** blade, select **No cloud apps, actions, or authentication contexts selected**, select the **Select apps** radio button, under the Select option select **None**, select **Office 365 Exchange Online**, and then click **Select**.

6. On the **New** blade, in the **Conditions** section, select **0 conditions selected**. 

7. In the list of conditions, under **Device platforms**, select **Not configured**. In the **Configure** section select **Yes**, select the **Select device platforms** radio button, select the **Windows** check box, and then select **Done**.

8. On the **New** blade under **Access controls**, in the **Grant** section, select **0 controls selected**. Select the **Require device to be marked as compliant** check box, and then select **Select**.

9. On the **New** blade, select **On** for the **Enable policy** option and then select **Create**.

10. Close Microsoft Edge.

## Task 2: Verify that the conditional access policy is working

1. Switch to **SEA-WS3** and sign in as **Admin** with the password of **Pa55w.rd**.

2. On **SEA-WS3**, on the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **outlook.office.com** and then press Enter.

4. On the pick an account dialog box, select **`Aaron@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter **Pa55w.rd1234** and select **Sign in**. If the Microsoft Edge Save password prompt appears, select **Update**.

6. Verify that you receive the message **"Try signing in another way"**.

7. Select **More details**. You should see more information about why you are blocked. 

   _Note: This is because SEA-WS3 is not joined to Azure AD and not managed by Intune, so not marked as compliant._

8. **Close** the browser window.

9. Switch to **SEA-WS1**, and sign in as as Aaron Nicholls with the PIN **102938**. 

   > Note: SEA-WS1 is a managed Windows 11 device that is enrolled in Intune.

10. On the taskbar, select **Microsoft Edge**.

11. In Microsoft Edge, type **Outlook.office.com** and then press Enter. 

12. Verify that you can access Aaron's mailbox. 

    _Note: This is because SEA-WS1 is a managed device and marked as compliant._

13. Close Microsoft Edge and sign out of SEA-WS1.

### Task 3: Disable the conditional access policy

1. Switch to **SEA-SVR1**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the  address bar, and then 
   press **Enter**.

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **All devices**.

   > Notice that SEA-WS1 is compliant, which is why Aaron was allowed to access his mailbox.

6. From the navigation pane select **Devices**, then select **Conditional access**.

7. On the **Conditional Access** page, select **Conditional1**.

8. On the **Conditional1** page, at the bottom of the page, select **Off** and then select **Save**.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured a conditional access policy to determine device compliance.

**END OF LAB**
