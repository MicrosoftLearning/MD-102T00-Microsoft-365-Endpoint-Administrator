# Practice Lab 0102: Synchronizing Identities by using Microsoft Entra Connect 

## Summary

In this lab, you will configure synchronization from Active Directory Domain Services to Entra ID.

### Scenario

Contoso Corporation is currently managing users in both AD DS and Entra ID as separate processes. This is time consuming and has led to inconsistent information. You have been tasked with addressing this issue by connecting the two directories by using the Microsoft Entra Connect synchronization tool.

#### Task 1: Configure directory synchronization with Microsoft Entra Connect

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter `http://www.microsoft.com/en-us/download/details.aspx?id=47594`

4. On the Microsoft Entra Connecta page, select **Download**.

    > Azure AD Connect automatically downloads to the **Downloads** folder on SEA-SVR1.

5. Select **Open downloads folder** and then in the **Downloads** window, double-click **AzureADConnect.msi**.

6. In the **Microsoft Azure Active Directory Connect** wizard, on the **Welcome to Azure AD Connect** page, select the **I agree to the license terms and privacy notice** check box, and then select **Continue**.

7. On the **Express Settings** page, select **Customize**.

8. On the **Install required components** page, select **Install**.

9. On the **User sign-in** page, ensure that **Password Hash Synchronization** is selected, and then select **Next**.

10. On the **Connect to Azure AD** page, in the **USERNAME** and **PASSWORD** boxes, enter **admin@yourtenant.onmicrosoft.com**, and your provided password, and then select **Next**.

11. On the **Connect your directories** page, ensure that **Contoso.com** is listed under **FOREST**, and then select **Add Directory**.

12. In the **AD forest account** window, select the **Create New AD Account** option, and in the **ENTERPRISE ADMIN USERNAME** field, type **Contoso\\Administrator**, and then type **Pa55w.rd** in the **PASSWORD** field. Select **OK**, and then select **Next**.

13. On the **Azure AD sign-in configuration** page, ensure that in the **USER PRINCIPAL NAME** drop-down list, the **userPrincipalName** value is selected. 

14. Select **Continue without matching all UPN suffixes to verified domains** and then select **Next**.

15. On the **Domain and OU filtering** page, select **Sync selected domains and OUs**.

16. Expand **Contoso.com**, clear the checkbox next to **Contoso.com** and ensure that the only following check boxes are selected: **IT**, **Managers**, **Marketing**, **Research**, and **Sales**. Select **Next**.

17. On the **Uniquely identifying your users** page, select **Next**.

18. On the **Filter users and devices** page, select **Next**.

19. On the **Optional features** page, review available options, but do not make any changes. Ensure that **Password hash synchronization** is selected, and then select **Next**.

20. On the **Ready to configure** page, ensure that **Start the synchronization process when configuration completes** is selected, and then select **Install**.

21. When configuration is complete, select **Exit**.  

    > Note: At this time, synchronization of objects from your local Active Directory Domain Services (AD DS) and Entra ID begins. You should wait approximately 3-4 minutes for this process to complete. Or check progress in the Synchronization Service application.

22. Close all open windows.

#### Task 2: Verify synchronization in Entra ID

1. On the taskbar, select **Microsoft Edge**.

2. In the address bar, enter **https://entra.microsoft.com**.

3. At the Sign-in prompt, enter **admin@yourtenant.onmicrosoft.com** and then select **Next**.

4. At the Enter password page, enter the password for the Admin account and then select **Sign in**. 

   > Note: Check with your instructor on the password to use for signing in with the Admin account.

5. At the Save password prompt, select **Save**.

6. At the Stay signed in prompt, select **No**. The Entra admin center opens.

7. In the Microsoft Entra admin center, in the navigation pane, select **Users** > **All users**.

8. Verify that you see users from your local AD DS. Ensure that these users have the value **Yes** in the **On-premises sync enabled** column. 

9. In the Navigation pane, under **Identity**, select **Groups** > **All groups**. Verify that you see groups from your local AD DS. Ensure that these groups have the value **Windows Server AD** in the **Source** column.

10. Select the **Managers** group.

11. On the **Managers** group page, select **Members** and then ensure that you see users. 

    > Note that you cannot add to or remove members from this group, as it is sourced from the local AD DS. 

12. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully configured Azure AD Connect to synchronize identity from Active Directory Domain Services to Entra ID.

**END OF LAB**
