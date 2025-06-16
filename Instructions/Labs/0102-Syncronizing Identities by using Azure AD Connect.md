# Practice Lab 0102: Synchronizing Identities by using Microsoft Entra Connect 

## Summary

In this lab, you will configure synchronization from Active Directory Domain Services to Entra ID.

### Scenario

Contoso Corporation is currently managing users in both AD DS and Entra ID as separate processes. This is time consuming and has led to inconsistent information. You have been tasked with addressing this issue by connecting the two directories by using the Microsoft Entra Connect synchronization tool.

#### Task 1: Configure directory synchronization with Microsoft Entra Connect

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter `https://entra.microsoft.com`

4. In the left navigantion pane, expand **Identity** and the select **Show more**.

5. In the left navigation pane, expand **Hybrid management** and then select **Microsoft Entra Connect**.

6. On the **Microsoft Entra Connect | Get started** pane, select the **Manage** tab.

7. In the **Manage your infrastructure** page, select **Download Connect Sync Agent**.

8. Select **Accept terms & download**. 

    >**Note**: The AzureAConnect.msi file will now download in the background. You **will not** see the download occur. 

9. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

On the Microsoft Entra Connect page, select **Download**.

    > Azure AD Connect automatically downloads to the **Downloads** folder on SEA-SVR1.

10. Select **Open downloads folder** and then in the **Downloads** window, double-click **AzureAdConnect.msi**.

11. In the **Microsoft Entra Connect Sync** wizard, on the **Welcome to Microsoft Entra Connect Sync** page, select the **I agree to the license terms and privacy notice** check box, and then select **Continue**.

12. On the **Express Settings** page, select **Customize**.

13. On the **Install required components** page, select **Install**.

14. On the **User sign-in** page, ensure that **Password Hash Synchronization** is selected, and then select **Next**.

15. On the **Connect to Microsoft Entra ID** page, in the **USERNAME** boxes, enter **admin@yourtenant.onmicrosoft.com**, and then select **Next**.

16. In the **Sign in to your account** window, enter **admin@yourtenant.onmicrosoft.com**, select **Next**, then enter your tenant password, and select **Sign in**.

17. On the **Connect your directories** page, ensure that **Contoso.com** is listed under **FOREST**, and then select **Add Directory**.

18. In the **AD forest account** window, select the **Create New AD Account** option, and in the **ENTERPRISE ADMIN USERNAME** field, type **Contoso\\Administrator**, and then type **Pa55w.rd** in the **PASSWORD** field. Select **OK**, and then select **Next**.

19. On the **Microsoft Entra sign-in configuration** page, ensure that in the **USER PRINCIPAL NAME** drop-down list, the **userPrincipalName** value is selected. 

20. Select **Continue without matching all UPN suffixes to verified domains** and then select **Next**.

21. On the **Domain and OU filtering** page, select **Sync selected domains and OUs**.

22. Expand **Contoso.com**, clear the checkbox next to **Contoso.com** and ensure that the only following check boxes are selected: **IT**, **Managers**, **Marketing**, **Research**, and **Sales**. Select **Next**.

23. On the **Uniquely identifying your users** page, select **Next**.

24. On the **Filter users and devices** page, select **Next**.

25. On the **Optional features** page, review available options, but do not make any changes. Ensure that **Password hash synchronization** is selected, and then select **Next**.

26. On the **Ready to configure** page, ensure that **Start the synchronization process when configuration completes** is selected, and then select **Install**.

27. When configuration is complete, select **Exit**.  

    > Note: At this time, synchronization of objects from your local Active Directory Domain Services (AD DS) and Entra ID begins. You should wait approximately 3-4 minutes for this process to complete. Or check progress in the Synchronization Service application.

28. Close all open windows.

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
