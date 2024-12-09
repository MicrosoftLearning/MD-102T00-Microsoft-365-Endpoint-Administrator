# Practice Lab09: Manage User & Device Security in Intune

## Summary

In this lab, you will configure per-user multi-factor authentication (MFA) and apply MFA using a conditional access policy .

### Prerequisites

> Note: You will need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 3: Configure multi-factor authentication using conditional access

### Scenario

To provide additional security for user sign on events, you need to configure and test multi-factor authentication (MFA). You decide that using a conditional access policy provides greater flexibility for your MFA requirements. Alex Wilber has agreed to validate the settings for you. 

### Task 1: Validate sign-in before enabling conditional access with MFA

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**.

6. On the **Stay signed in** page, select **No**. 

   > Outlook opens to Alex's inbox. Take note that only the password was required to sign in to Outlook on the Web as you removed the MFA in the previous Exercise.

7. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

8. Close Microsoft Edge.

### Task 2: Configure conditional access with MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. In the navigation pane, expand **Protection** page, and then select **Conditional Access**.

5. On the **Conditional Access** page, select **Policies**, and then select **+ New policy**.

6. On the **New Conditional access policy** page, in the **Name** box, enter **Contoso MFA Policy**.

7. Under **Assignments**, select **0 users and groups selected**.

8. In the Users and groups pane, select the option next to **Select users and groups** and then select the check box next to **Users and groups**.

9. On the **Select users and groups** page, select **Alex Wilber** and then select **Select**. 

    > Note that typically you would specify a group, however for this exercise we will just test the setting on Alex Wilber.

10. Select **No target resources selected** and then click **Select apps**.

    > Note the Control access based on client app setting. This setting allows you to specify the client app that is used to access the resource. For example, you can specify that only the Outlook app can be used to access Exchange Online. 

11. On the **Select** section of the page, click **None**.

12. On the **Select** page, select the check box next to **Office 365** and then click **Select**.

13. Under **Access controls**, in the **Grant** section, select **0 controls selected**.

14. On the **Grant** page, select **Grant access**, select the check box next to **Require multifactor authentication**, and then click **Select**.

15. Under **Enable policy**, select **On**.

16. Select **Create** to create the Contoso MFA Policy. Notice that the policy is listed with a State of **On**.

17. Close Microsoft Edge.

### Task 3: Validate conditional access MFA

1. Switch to **SEA-WS3**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **https://outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**. 

6. At the Verify your identity prompt, select your phone number.

   > The Enter code dialog box opens.

7. At the **Enter code** page, enter the code sent to your mobile phone, and then select **Verify**.

8. At the Stay signed in message, select **No**. 

   > Outlook on the Web opens to Alex Wilber's inbox.

9. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

10. Close Microsoft Edge.

### Task 4: Remove conditional access MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. In the Microsoft Entra admin center, in the navigation pane, expand **Protection** and then select **Conditional Access**.

5. On the **Conditional Access** page, select **Policies** and then select **Contoso MFA Policy**.

6. On the **Contoso MFA Policy** page, select **Delete**.

7. At the **Are you sure?** prompt, select **Yes**.

8. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured multi-factor authentication by using a conditional access policy.

**END OF LAB**