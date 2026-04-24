---
lab:
  title: 'Practice Lab 0102: Synchronizing Identities by using Microsoft Entra Connect'
  description: In this lab, you will configure synchronization from Active Directory Domain Services to Entra ID.
  duration: 20 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Entra
    - Active Directory
---

# Practice Lab 0102: Synchronizing Identities by using Microsoft Entra Connect 

## Summary

In this lab, you will configure synchronization from Active Directory Domain Services to Entra ID.

### Scenario

Contoso Corporation currently manages users in both AD DS and Microsoft Entra ID as separate processes. This is time consuming and has led to inconsistent information. Your task is to address this issue by connecting the two directories by using the Microsoft Entra Connect synchronization tool.

#### Task 1: Configure directory synchronization with Microsoft Entra Connect

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In the address bar, enter `https://entra.microsoft.com`.

4. In the left navigation pane, under **Entra ID**, select **Entra Connect**.

5. On the **Microsoft Entra Connect | Get started** pane, select the **Manage** tab.

6. On the **Manage your infrastructure** page, select **Download Connect Sync Agent**.

7. Select **Accept terms & download**.

    > [!NOTE]
    > Microsoft Entra Connect Sync automatically downloads to the **Downloads** folder on SEA-SVR1.

8. Select **Open downloads folder**, and then in the **Downloads** window, open **AzureAdConnect.msi**.

9. In the **Microsoft Entra Connect Sync** wizard, on the **Welcome to Microsoft Entra Connect Sync** page, select the **I agree to the license terms and privacy notice** check box, and then select **Continue**.

10. On the **Express Settings** page, select **Customize**.

    > [!NOTE]
    > Do not select **Use express settings**.

11. On the **Install required components** page, select **Install**.

12. On the **User sign-in** page, ensure that **Password Hash Synchronization** is selected, and then select **Next**.

13. On the **Connect to Microsoft Entra ID** page, in the **USERNAME** box, enter **admin@yourtenant.onmicrosoft.com**, and then select **Next**.

14. In the **Sign in to your account** window, enter **admin@yourtenant.onmicrosoft.com**, select **Next**, enter your tenant password, and then select **Sign in**.

15. On the **Connect your directories** page, ensure that **Contoso.com** is listed under **FOREST**, and then select **Add Directory**.

16. In the **AD forest account** window, select the **Create New AD Account** option. In the **ENTERPRISE ADMIN USERNAME** field, enter **Contoso\\Administrator**, and in the **PASSWORD** field, enter **Pa55w.rd**. Select **OK**, and then select **Next**.

17. On the **Microsoft Entra sign-in configuration** page, ensure that in the **USER PRINCIPAL NAME** drop-down list, the **userPrincipalName** value is selected.

18. Select **Continue without matching all UPN suffixes to verified domains**, and then select **Next**.

19. On the **Domain and OU filtering** page, select **Sync selected domains and OUs**.

20. Expand **Contoso.com**, clear the checkbox next to **Contoso.com**, and ensure that only the following check boxes are selected: **IT**, **Managers**, **Marketing**, **Research**, and **Sales**. Select **Next**.

21. On the **Uniquely identifying your users** page, select **Next**.

22. On the **Filter users and devices** page, select **Next**.

23. On the **Optional features** page, review the available options but do not make any changes. Ensure that **Password hash synchronization** is selected, and then select **Next**.

24. On the **Ready to configure** page, ensure that **Start the synchronization process when configuration completes** is selected, and then select **Install**.

25. When configuration is complete, select **Exit**.

    > [!NOTE]
    > Synchronization of objects from your local Active Directory Domain Services (AD DS) and Microsoft Entra ID begins at this point. Wait approximately 3-4 minutes for this process to complete, or check progress in the **Synchronization Service** application.

26. Close all open windows.

#### Task 2: Verify synchronization in Entra ID

1. In the Microsoft Entra admin center, in the navigation pane, select **Users**.

2. Verify that you see users from your local AD DS. Ensure that these users have the value **Yes** in the **On-premises sync enabled** column.

3. In the navigation pane, select **Groups**, and then select **All Groups**. Verify that you see groups from your local AD DS. Ensure that these groups have the value **Windows Server AD** in the **Source** column. You need to scroll right using the horizontal scroll bar to see the **Source** column.

4. Select the **Managers** group.

5. On the **Managers** group page, select **Members**, and then verify that you see users.

    > [!NOTE]
    > You cannot add or remove members from this group because it is sourced from the local AD DS.

6. Close Microsoft Edge.

**Results**: After completing this exercise, you have successfully configured Microsoft Entra Connect to synchronize identities from Active Directory Domain Services to Microsoft Entra ID.

**END OF LAB**
