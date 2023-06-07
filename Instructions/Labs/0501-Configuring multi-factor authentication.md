# Practice Lab: Configuring Multi-factor Authentication

## Summary

In this lab, you will configure per-user multi-factor authentication (MFA) and apply MFA using a conditional access policy .

### Prerequisites

You will need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

## Exercise 1: Configure per-user multi-factor authentication

### Scenario

To provide additional security for user sign on events, you need to configure and test multi-factor authentication (MFA). You decide to first test out per-user MFA. Alex Wilber has agreed to validate the settings for you. 

### Task 1: Validate sign-in before enabling MFA

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. At the **Sign in** page, enter **`AlexW@yourtenant.onmicrosoft.com`** and then select **Next**.

5. On the **Enter password** page, enter **Pa55w.rd** and select **Sign in**. At the Edge Save password prompt, select **Save**.

6. At the **Stay signed in** prompt, select **No**.

   > Outlook on the Web opens. Take note that only the password was required to sign in to Outlook on the Web.

7. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

8. Close Microsoft Edge.

### Task 2: Enable MFA for a user

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

3. On the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

4. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

5. In the Microsoft Entra admin center, in the navigation pane, select **Users**.

6. In the search resources box, type multifactor authentication and then select **multifactor authentication**.

   > The multi-factor authentication page opens.

7. Select **Additional cloud-based multifactor authentication settings**.

8. In the **multi-factor authentication** page, select **service settings**. Select **Allow users to remember multi-factor authentication on devices they trust**.

9. Next to **Number of days users can trust devices for**, enter **30** and then select **save**. 

10. Close the **multi-factor authentication** page.

11. In the navigation pane, select **All users**.

12. At the top of the user list, select Per-user MFA.

   > The Per-user MFA page opens.

13. In the user list, select the check box next to **Alex Wilber**.

14. On the **quick steps** pane, select **enable**.

15. On the **About enabling multi-factor auth** message, select **enable multi-factor auth**.

16. On the **Updates successful** message, select **close**. Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **Enabled**.

17. Close Microsoft Edge.

### Task 3: Register and Validate MFA

1. Switch to **SEA-WS3**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**.

6. At the **More information required** page, select **Next**. The Keep you account secure page opens.

   > Typically, you will want to use the Microsoft Authenticator app to manage multi-factor authentication. However for this lab scenario, you will use text messages.

7. On the **Keep your account secure** page, enter your mobile phone number which you can receive text messages, and then select **Next**.

8. After you receive the verification code as a text message, enter the code where indicated on the **Keep your account secure** page and then select **Next**.

9. on the **Keep your account secure** page, you will recieve a mesage "Great job! You have successfully set up your account for multi-factor authentication. Choose **Done** to continue signing in." Select **Done**.

10. You will be redirected to a verification page.

11. You will receive a text message with a verification code. Enter the code on the verification page and select **Verify**.

    > The **Stay signed in** page opens.

12. At the Stay signed in message, select **No**. 

    > Outlook on the Web opens to Alex Wilber's inbox.

13. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

14. Close Microsoft Edge.

### Task 3: Remove per-user MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Users**.

5. Select **All users** and then at the top of the results pane select **Per-user MFA**. 
   
   > The Per-user MFA page opens.

6. In the user list, select the check box next to **Alex Wilber**.

7. On the **quick steps** pane, select **disable**.

8. On the **About disabling multi-factor auth** message, select **disable multi-factor auth**.

9. On the **Updates successful** message, select **close**. Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **Disabled**.

10. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured per-user multi-factor authentication.

## Exercise 2: Configure multi-factor authentication using conditional access

### Scenario

To provide additional security for user sign on events, you need to configure and test multi-factor authentication (MFA). You decide that using a conditional access policy provides greater flexibility for your MFA requirements. Alex Wilber has agreed to validate the settings for you. 

### Task 1: Validate sign-in before enabling conditional access with MFA

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**.

6. On the **Stay signed in** page, select **No**. 

   > Outlook opens to Alex's inbox. Take note that only the password was required to sign in to Outlook on the Web.

7. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

8. Close Microsoft Edge.

### Task 2: Configure conditional access with MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. In the Microsoft Entra admin center, in the navigation pane, select **Protect and Secure**.

5. On the **Protect and Secure** page, select **Conditional Access**.

6. On the **Conditional Access** page, select **Policies**, select **New policy**, and then select **Create new policy**.

7. On the **New Conditional access policy** page, in the **Name** box, enter **Contoso MFA Policy**.

8. Under **Assignments**, select **0 users and groups selected**.

9. In the Users and groups pane, select the option next to **Select users and groups** and then select the check box next to **Users and groups**.

10. On the **Select users and groups** page, select **Alex Wilber** and then select **Select**. 

    > Note that typically you would specify a group, however for this exercise we will just test the setting on Alex Wilber.

11. Select **No cloud apps, actions, or authentication contexts selected** and then click **Select apps**.

    > Note the Control access based on client app setting. This setting allows you to specify the client app that is used to access the resource. For example, you can specify that only the Outlook app can be used to access Exchange Online. 

12. On the **Select** section of the page, click **None**.

13. On the **Select** page, select the check box next to **Office 365** and then click **Select**.

14. Under **Access controls**, in the **Grant** section, select **0 controls selected**.

15. On the **Grant** page, select **Grant access**, select the check box next to **Require multi-factor authentication**, and then click **Select**.

16. Under **Enable policy**, select **On**.

17. Select **Create** to create the Contoso MFA Policy. Notice that the policy is listed with a State of **On**.

18. Close Microsoft Edge.

### Task 3: Validate conditional access MFA

1. Switch to **SEA-WS3**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**. 

6. At the Verify your identity prompt, select your phone number.

   > The Enter code dialog box opens. Notice that "don't ask again for 90 days" is selected by default.

7. At the **Enter code** page, enter the code sent to your mobile phone, and then select **Verify**.

8. At the Stay signed in message, select **No**. 

   > Outlook on the Web opens to Alex Wilber's inbox.

9. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

10. Close Microsoft Edge.

### Task 4: Remove conditional access MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https:EntAdmin.microsoft.com**, and then press **Enter**.

3. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The EntAdmin admin center opens.

4. In the Entrada admin center, in the navigation pane, under **protect and secure** select **Conditional Access**.

5. On the **Conditional Access** page, select **Policies** and then select **Contoso MFA Policy**.

6. On the **Contoso MFA Policy** page, select **Delete**.

7. At the **Are you sure?** prompt, select **Yes**.

8. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured multi-factor authentication by using a conditional access policy.

**END OF LAB**
