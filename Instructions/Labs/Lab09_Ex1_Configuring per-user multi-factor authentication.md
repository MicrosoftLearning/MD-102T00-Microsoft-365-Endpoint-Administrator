# Practice Lab09: Manage User & Device Security in Entra & Intune

## Summary

In this lab, you will configure per-user multi-factor authentication (MFA) and apply MFA using a conditional access policy .

### Prerequisites

> Note: You will need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 2: Configure per-user multi-factor authentication

### Scenario

To provide additional security for user sign on events, you need to configure and test multi-factor authentication (MFA). You decide to first test out per-user MFA. Alex Wilber has agreed to validate the settings for you. 

### Task 1: Validate sign-in before enabling MFA

1. Sign in to **MD102-WS9** as **Admin** with the password **Pa55w.rd**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. At the **Sign in** page, enter **`AlexW@yourtenant.onmicrosoft.com`** and then select **Next**.

5. On the **Enter password** page, enter the tenant password provided by your instructor and select **Sign in**. At the Edge Save password prompt, select **Save & Turn on**.

6. At the **Stay signed in** prompt, select **No**.

   > Outlook on the Web opens. Take note that only the password was required to sign in to Outlook on the Web.

7. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

8. Close Microsoft Edge.

### Task 2: Enable MFA for a user

1. Switch to **MD102-WS1**.

2. On **MD102-WS1**, if necessary, sign in as **Admin** with the password of **Pa55w.rd**.

3. On the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

4. Sign in as user **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

5. At the top of the web page, In the search resources box, type multifactor authentication and then select **multifactor authentication**.

   > The multi-factor authentication page opens.

6. Select **Additional cloud-based multifactor authentication settings**.

7. In the **multi-factor authentication** page, select **service settings**. Select **Allow users to remember multi-factor authentication on devices they trust**.

8. Next to **Number of days users can trust devices for**, enter **30** and then select **save**. 

9. Close the **multi-factor authentication** page.

10. Navigate back to the **Microsoft Entra admin center** Edge tab and in the navigation pane, select **Users** > **All users**.

11. At the top of the user list, select Per-user MFA.

   > The Per-user MFA page opens.

12. In the user list, select the check box next to **Alex Wilber**.

13. On the **quick steps** pane, select **Enable MFA**.

14. On the **About enabling multi-factor auth** message, select **enable multi-factor authentication**.

15. On the **Updates successful** message, select **close**. Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **enabled**.

16. Close Microsoft Edge.

### Task 3: Register and Validate MFA

1. Switch to **MD102-WS9**. 

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter **outlook.office.com** and press Enter.

4. On the **Pick an account** page, select **`AlexW@yourtenant.onmicrosoft.com`**.

5. On the **Enter password** page, enter the tenant password and select **Sign in**.

6. At the **More information required** page, select **Next**. The Keep your account secure page opens.

7. On the **Keep your account secure** page, select **Next**.

8. Select **Next**, scan the QR code and **finish** the Authenticator setup.

9.  On the verification page, select **Next** and then select **Done**.

10. At the Stay signed in message, select **No**. 

    > Outlook on the Web opens to Alex Wilber's inbox.

11. At the top-right corner, select the **Account manager for Alex Wilber** and then select **Sign out**.

12. Close Microsoft Edge.

### Task 3: Remove per-user MFA

1. Switch to **MD102-WS1**.

2. On **MD102-WS1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com**, and then press **Enter**.

3. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

4. In the Microsoft Entra admin center, in the navigation pane, select **Users**.

5. Select **All users** and then at the top of the results pane select **Per-user MFA**. 
   
   > The Per-user MFA page opens.

6. In the user list, select the check box next to **Alex Wilber**.

7. On the **quick steps** pane, select **Disable**.

8. On the **Disable multi-factor authentication?** message, select **yes**.

9. On the **Updates successful** message, select **close**. Take note that the **Multi-Factor Auth Status** for Alex Wilber is now **Disabled**.

10. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured per-user multi-factor authentication.

**End of LAB**
