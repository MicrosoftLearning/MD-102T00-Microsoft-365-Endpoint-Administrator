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

5. On the **Enter password** page, enter the tenant password and select **Sign in**. At the Edge Save password prompt, select **Save**.

6. At the **Stay signed in** prompt, select **No**.

   > Outlook on the Web opens. Take note that only the password was required to sign in to Outlook on the Web.

7. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

8. Close Microsoft Edge.

### Task 2: Enable MFA for a user

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

3. On the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

4. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

5. In the Azure Active Directory admin center, in the navigation pane, select **Users**.

6. Select **All users** and then at the top of the results pane select **Per-user MFA**. You may need to select the ellipse first to view the **Per-user MFA** option.

7. On the multi-factor authentication page, select **service settings**.

8. Scroll down to the **verification options** section. 

   > Take note of the various methods that can be configured for user verification. 

9. In the **remember multi-factor authentication on trusted device** section, select the check box next to **Allow users to remember multi-factor authentication on devices they trust**.

10. Next to **Number of days users can trust devices for**, enter **30** and then select **save**. Select **close** when prompted.

11. At the top of the page, under **multi-factor authentication**, select **users**.

12. In the user list, select the check box next to **Alex Wilber**.

13. In the Alex Wilber page, select **Enable**.

14. On the **About enabling multi-factor auth** message, select **enable multi-factor auth**.

15. On the **Updates successful** message, select **close**. Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **Enabled**.

16. Close Microsoft Edge.

### Task 3: Register and Validate MFA

1. Switch to **SEA-WS3**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**.

6. At the **More information required** page, select **Next**. The Keep you account secure page opens.

   > Typically, you will want to use the Microsoft Authenticator app to manage multi-factor authentication. However for this lab scenario, you will use text messages.

7. On the **Keep your account secure** page, select **I want to set up a different method**.

8. In the **Choose a different method** dialog box, select **Phone**, and then select **Confirm**.

9. On the **Phone** page, enter your mobile phone number which you can receive text messages, and then select **Next**.

10. After you receive the verification code as a text message, enter the code where indicated on the **Phone** page and then select **Next**.

11. At the SMS verified message, select **Next** and then select **Done**.

12. At the Stay signed in message, select **No**. 

    > Outlook on the Web opens to Alex Wilber's inbox.

13. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

14. Close Microsoft Edge.

_Note: Users only have to register the first time they use MFA. Subsequent sign-ins only require providing the validation code which it texted to the phone number that you entered during registration._

15. On the taskbar, select **Microsoft Edge**.

16. In the address bar, enter **outlook.office.com** and press Enter.

17. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

18. On the **Enter password** page, enter the tenant password and select **Sign in**. 

    > The **Verify your identity** prompt opens. Notice that it contains the last two digits of your phone number.

19. At the **Verify your identity** prompt, select your Text phone number.

20. At the **Enter code** page, enter the code sent to your mobile phone, and then select **Verify**.

    > Notice that you can select a check box to not ask for verification again for 30 days.

21. At the Stay signed in message, select **No**. Outlook on the Web opens to Alex Wilber's inbox.

22. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

23. Close Microsoft Edge.

### Task 3: Remove per-user MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Users**.

5. Select **All users** and then at the top of the results pane select **Per-user MFA**. You may need to select the ellipse first to view the **Per-user MFA** option.

6. At the top of the page, under **multi-factor authentication**, select **users**.

7. In the user list, select the check box next to **Alex Wilber**. 

   > Take note that the **Multi-Factor Auth Status** for Alex Wilber is now set to **Enforced** (was previously set to Enabled). This is because Alex has registered and is using MFA.

8. In the Alex Wilber page, select **Manage user settings.**

9. On the Manage user settings box, select the check box next to all three options, select **save** and then select **close**.

   > These options will remove all saved MFA settings for Alex.

10. In the user list, select the check box next to **Alex Wilber**. 

11. In the Alex Wilber page, select **Disable**.

12. On the **Disable multi-factor authentication** message, select **yes**.

13. On the **Updates successful** message, select **close**. 

    > Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **Disabled**.

14. Close Microsoft Edge.

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

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Azure Active Directory**.

5. On the **Contoso** navigation pane, select **Security**.

6. On the **Security** page, select **Conditional Access**.

7. On the **Conditional Access** page, select **Policies**, select **New policy**, and then select **Create new policy**.

8. On the **New Conditional access policy** page, in the **Name** box, enter **Contoso MFA Policy**.

9. Under **Assignments**, select **0 users or workload identities selected**.

10. In the Users and groups pane, select the option next to **Select users and groups** and then select the check box next to **Users and groups**.

11. On the **Select** page, select **Alex Wilber** and then click **Select**. 

    > Note that typically you would specify a group, however for this exercise we will just test the setting on Alex Wilber.

12. Select **No cloud apps, actions, or authentication contexts selected** and then click **Select apps**.

13. On the **Select** page, select the check box next to **Office 365** and then click **Select**.

14. Under **Access controls**, in the **Grant** section, select **0 controls selected**.

15. On the **Grant** page, select **Grant access**, select the check box next to **Require multi-factor authentication**, and then click **Select**.

16. Under **Enable policy**, select **On**.

17. Select **Create** to create the Contoso MFA Policy. Notice that the policy is listed with a State of **On**.

18. In the Azure Active Directory admin center, select **Users**.

19. In the User list, select **Alex Wilber**.

20. On the Alex Wilber page, select **Authentication methods**. 

    > Notice that a phone number has already been configured for Alex, but it is not enabled. This was because he registered MFA during the previous lab. However, you removed this method when you managed Alex's per-user MFA settings.

21. In the message box, under your phone number, select **Enable**.

22. Close Microsoft Edge.

### Task 3: Validate conditional access MFA

1. Switch to **SEA-WS3**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**. 

6. At the Verify your identity prompt, select your phone number.

   > The Enter code dialog box opens. Notice that you can select a check box to specify Don't ask again for 30 days.

7. At the **Enter code** page, enter the code sent to your mobile phone, and then select **Verify**.

8. At the Stay signed in message, select **No**. 

   > Outlook on the Web opens to Alex Wilber's inbox.

9. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

10. Close Microsoft Edge.

### Task 4: Remove conditional access MFA

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://aad.portal.azure.com**, and then press **Enter**.

3. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Azure Active Directory admin center opens.

4. In the Azure Active Directory admin center, in the navigation pane, select **Azure Active Directory**.

5. On the **Contoso** navigation pane, select **Security**.

6. On the **Security** page, select **Conditional Access**.

7. On the **Conditional Access** page, select **Policies** and then select **Contoso MFA Policy**.

8. On the **Contoso MFA Policy** page, select **Delete** and then select **Yes**.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured multi-factor authentication by using a conditional access policy.

**END OF LAB**
