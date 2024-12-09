# Practice Lab03: Manage Windows Device Compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

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

5. On the **Enter password** page, enter **Pa55w.rd1234!** and select **Sign in**. If the Microsoft Edge Save password prompt appears, select **Update**.

6. You should receive a message that ask you to switch Edge profile. Select **Switch Edge profile**.

7. You will be prompted with a message stating, "**Continue with your work or school account**". Select Sign in to sync data.

8. You will be required to enter your password again. Enter **Pa55w.rd1234!** and select **Sign in**.

9. A message will appear stating, "**Stay signed in to all your Microsoft apps**". Select **no, sign in to this app only**.

    > Note: A prompt will appear stating, "**Allow my organization to manage my device**". This is because SEA-WS3 is not joined to Entra ID and not managed by Intune. As such, you are unable to access Aarons' mailbox from this device.

10. **Close** all windows and sign out of **SEA-WS3**.

11. Switch to **SEA-WS1**, and sign in as as Aaron Nicholls with the PIN **102938**. 

    > Note: SEA-WS1 is a managed Windows 11 device that is enrolled in Intune.

12. On the taskbar, select **Microsoft Edge**.

13. In Microsoft Edge, type **outlook.office.com** and then press Enter. 

14. Verify that you can access Aaron's mailbox. 

    > Note: This is because SEA-WS1 is a managed device and marked as compliant._

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
