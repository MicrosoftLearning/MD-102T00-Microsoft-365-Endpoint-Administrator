# Practice Lab 0101: Managing Identities in Entra ID

## WWL Tenants - Terms of Use

If you are being provided with a tenant as a part of an instructor-led training delivery, please note that the tenant is made available for the purpose of supporting the hands-on labs in the instructor-led training.

Tenants should not be shared or used for purposes outside of hands-on labs. The tenant used in this course is a trial tenant and cannot be used or accessed after the class is over and are not eligible for extension.

Tenants must not be converted to a paid subscription. Tenants obtained as a part of this course remain the property of Microsoft Corporation and we reserve the right to obtain access and repossess at any time.

## Summary

In this lab, you will use the Entra admin center to create and modify users, assign administrative roles, create and modify groups, and manage license assignments in Entra ID.

## Exercise 1: Creating users in Entra ID

### Scenario

You need to create user accounts in Azure AD for new employees that will start next week. New users are listed in the following table:

| Name           | User Name                             | Password   | Job title        | Department |
| -------------- | ------------------------------------- | ---------- | ---------------- | ---------- |
| Edmund Reeve   | `ereeve@yourtenant.onmicrosoft.com`   | Pa55-w.rd! | HR Rep           | HR         |
| Miranda Snider | `msnider@yourtenant.onmicrosoft.com`  | Pa55-w.rd! | Helpdesk Manager | Operations |
| Cody Godinez   | `cgodinez@yourtenant.onmicrosoft.com` | Pa55-w.rd! | Sales Rep        | Sales      |

_Note: For location use either your local region or United States._

You've also been told that several more employees will be hired over the next couple of months. You've decided that scripting would be a far more efficient method of adding a large number of new users. You've decided to create a PowerShell script and test it out when you create Cody Godinez's account.

### Task 1: Create users by using the Microsoft Entra admin center

1. On **SEA-SVR1**, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

2. Close **Server Manager**.

3. On the taskbar, select **Microsoft Edge**.

4. In the address bar, enter **https://entra.microsoft.com**.

5. At the Sign-in prompt, enter **admin@yourtenant.onmicrosoft.com** and then select **Next**.

6. At the Enter password page, enter the password for the Admin account and then select **Sign in**.

   > Note: Check with your instructor on the password to use for signing in with the Admin account.

7. At the Save password prompt, select **Save & Turn on**.

8. At the Stay signed in prompt, select **No**. The Entra admin center opens.

9. In the Microsoft Entra admin center, in the navigation pane, select **Users**.

    > Take note of the users that already exist as members of the Microsoft Entra ID. The **On-premises sync enabled** column states **No** for all current users. This indicates that each user was created directly in Microsoft Entra ID and not synchronized from an on-premises directory service.

10. On the **Users | All users** page, select **New user** then select **Create new user**.

11. On the **Create new user** page, enter the following:

    - User Principal Name: **ereeve**
    - Display Name: **Edmund Reeve**

12. Uncheck **Auto-generated password**

13. Next to **Password**, enter **Pa55-w.rd!**.

    > Note: If you receive an error message stating that this password in weak or commonly used, enter the tenant password found under the **Resources** tab of this lab profile. Alternatively, you can enter a complex password of your choice.
    
14. Select **Next: Properties** located at the bottom of the page.

15. Next to **First name**, enter **Edmund**.

16. Next to **Last name**, enter **Reeve**.

17. Next to **User type**, make note that **Member** is selected.

    > Note: The **Member** user type is the default user type. This user type is used for most users in an organization.

18. Next to **Job title**, enter **HR Rep**.

19. Next to **Department**, enter **HR**.

20. Next to **Usage location**, select **United States**.

21. Select **Next: Assignments** located at the bottom of the page.

22. On the **Assignments** page, note that no assignments are selected.

    > By default, no groups are assigned to the user. This is because the user is not a member of any groups until you assign them.

23. Select **Next: Review + create** located at the bottom of the page.
    > Review the information on this page to ensure that it is correct.

24. Select **Create**.

25. On the **Users | All users** page, select **New user** then select **Create new user**.

26. On the **Create new user** page, enter the following:

    - User Principal Name: **msnider**
    - Display Name: **Miranda Snider**

27. Uncheck **Auto-generated password**

28. Next to **Password**, enter **Pa55-w.rd!**.

    > Note: If you receive an error message stating that this password in weak or commonly used, enter the tenant password found under the **Resources** tab of this lab profile. Alternatively, you can enter a complex password of your choice.

29. Select **Next: Properties** located at the bottom of the page.

30. Next to **First name**, enter **Miranda**.

31. Next to **Last name**, enter **Snider**.

32. Next to **User type**, make note that **Member** is selected.

33. Next to **Job title**, enter **Helpdesk Manager**.

34. Next to **Department**, enter **Operations**.

35. Next to **Usage location**, select **United States**.

36. Select **Next: Assignments** located at the bottom of the page.

37. On the **Assignments** page, note that no assignments are selected.

38. Select **Next: Review + create** located at the bottom of the page.

39. Select **Create**.

40. Minimize the **Microsoft Edge** window.

### Task 2: Create users by using PowerShell

# Steps to install PowerShell 7.5.2 on SEA-SVR1

1. On **SEA-SVR1**, open **Microsoft Edge**.  

2. In the address bar, enter **https://github.com/PowerShell/powershell/releases/download/v7.5.2/PowerShell-7.5.2-win-x64.msi**  

3. On the taskbar, select **File Explorer**, then navigate to your **Downloads** folder.  

4. Double-click **PowerShell-7.5.2-win-x64.msi** to launch the setup wizard.  

   - Select **Next**  
   - Leave the **Destination Folder** as is, then select **Next**  
   - Leave the **Optional Actions** as is, then select **Next**  
   - Leave the checkboxes blank under *Use Microsoft Update to help keep your computer secure and up to date*, then select **Next**  
   - Select **Install**  

5. On the **Installation completed successfully** window, check **Launch PowerShell**, then select **Finish**.  

   > **Note:** If the installer closed without launching PowerShell, click the **Windows Search** bar, type **pwsh**, right-click **PowerShell 7**, and select **Run as administrator**.  

6. In the **PowerShell 7** window, type the following command, and then press **Enter**. If prompted, enter **Y** at the NuGet and repository messages:

    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```

7. In the **PowerShell 7** window, type the following command, and then press **Enter**:

    ```powershell
    Connect-MgGraph -scopes "user.readwrite.all, group.readwrite.all"
    ```

8. A new tab in **Microsoft Edge** will appear prompting you to sign in. In the **Sign in to your account** dialog box, sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant password, and then select **Sign in**.

9. On the **Permissions Requested** prompt that appears, check **Consent on behalf of your organization** and then select **Accept**.

10. Close out of the **Authentication complete** tab and then minimize **Microsoft Edge**

11. Back In the **PowerShell 7** window, type the following code to create a new profile object, and then press **enter**. Replace **Pa55w.rd** with a complex password of your choice:

    ```powershell
    $PWProfile = @{
        Password = "Pa55w.rd";
        ForceChangePasswordNextSignIn = $false
    }
    ```
    
12. Next, type the following code to create a new user, and then press **Enter**. Ensure "yourtenant" matches your assigned tenant name:

    ```powershell
    New-MgUser `
        -DisplayName "Cody Godinez" `
        -GivenName "Cody" -Surname "Godinez" `
        -MailNickname "cgodinez" `
        -UsageLocation "US" `
        -UserPrincipalName "cgodinez@yourtenant.onmicrosoft.com" `
        -PasswordProfile $PWProfile -AccountEnabled `
        -Department "Sales" -JobTitle "Sales Rep"
    ```

13. To confirm that the user **Cody Godinez** was created, In the **PowerShell 7** window, type the following command and then press **Enter**:

    ```powershell
    Get-MgUser
    ```

> Verify that the list of users from your tenant is displayed. 

**Results**: After completing this exercise, you will have successfully created new user accounts in Entra ID.

## Exercise 2: Assigning Administrative Roles in Entra ID

### Scenario

You need to review and modify the current administrative roles for your tenant.

You have been provided a list of users should have administrative roles assigned as indicated in the following table.  

| Name           | Must be able to:                         | Administrative Role needed: |
| -------------- | ---------------------------------------- | --------------------------- |
| Allan Deyoung  | Manage the tenant                        | Global administrator        |
| Edmund Reeve   | Manage users, group, and password resets | User administrator          |
| Miranda Snider | Manage password resets                   | Helpdesk administrator      |

### Task 1: Review and Assign Administrative Roles

1. On SEA-SVR1, switch to Microsoft Edge.

2. In the Microsoft Entra admin center, in the Navigation pane, select **Roles & admins**.

    > Note that you can scroll down the list or use the search box to find the **Role** you are looking for.

3. Using the search box, search for **Global administrator**.

4. Select **Global administrator** (select the name, not the checkbox).

5. In the **Global administrator** pane, select **+ Add assignments**.

6. Under **Select members**, select **No member selected**, then search for and select **Allan Deyoung**.

7. Select **Add**.

8. In the navigation breadcrumbs, select **Roles & administrators | All roles**.

9. Using the search box, search for **User administrator**.

10. Select **User administrator**.

11. In the **User administrator** pane, select **+ Add assignments**.

12. Under **Select members**, select **No member selected**, then search for and select **Edmund Reeve**.

13. Select **Add**.

14. In the navigation breadcrumbs, select **Roles & administrators | All roles**.

15. Using the search box, search for **Helpdesk administrator**.

16. Select **Helpdesk administrator**.

17. In the **Helpdesk administrator** pane, select **+ Add assignments**

18. Under **Select members**, select **No member selected**, then search for and select **Miranda Snider**.

19. Select **Add**.

20. In the navigation pane, select **Home**.

**Results**: After completing this exercise, you should have successfully assigned administrative roles to users.

## Exercise 3: Creating and managing groups and validating license assignment

### Scenario

You need to add the three new users to a Security group and assign licenses as indicated in the following table.  

| Name           | Member of:       | License to assign                                            |
| -------------- | ---------------- | ------------------------------------------------------------ |
| Edmund Reeve   | Contoso_Managers | Office 365 E5, Enterprise Mobility + Security E5 via group membership |
| Miranda Snider | Contoso_Managers | Office 365 E5, Enterprise Mobility + Security E5 via group membership |
| Cody Godinez   | Contoso_Sales    | Office 365 E5, Enterprise Mobility + Security E5 via group membership direct assignment |

You also been asked to modify the Company branding for the sign-in page.

### Task 1: Create groups by using the Microsoft Entra admin center

1. On **SEA-SVR1**, in the Microsoft Entra admin center, in the navigation pane, select **Groups**.

2. Select **New group**.

3. On the **New Group** page, enter the following:

    - Group type: **Security**
    - Group name: **Contoso_Managers**
    - Membership type: **Assigned**

4. Under Members, select **No members selected**.

5. In the Add members page add **Edmund Reeve**, **Miranda Snider**, and then click **Select**.

6. Select **Create**.

### Task 2: Create groups by using PowerShell

1. On SEA-SVR1, switch to PowerShell 7.

2. In the **PowerShell 7** window, type the following code to create a new group, and then press **Enter**:

    ```powershell
    New-MgGroup -DisplayName "Contoso_Sales" -Description "Contoso Sales team users" -MailEnabled:$false -Mailnickname "Contoso_Sales" -SecurityEnabled
    ```

3. In the **PowerShell 7** window, type the following command, and then press **Enter**:

    ```powershell
    Get-MgGroup
    ```

4. Verify that you get the list of groups in your tenant, including the Contoso_Sales group you just created.

5. In the **PowerShell 7** window, type the following code to define a variable as the Contoso_Sales group, and then press **Enter**:

    ```powershell
    $group = Get-MgGroup | Where-Object {$_.DisplayName -eq "Contoso_Sales"}
    ```

6. In the **PowerShell 7** window, type the following code to define another variable as the user, and then press **Enter**:

    ```powershell
    $user = Get-MgUser | Where-Object {$_.DisplayName -eq "Cody Godinez"}
    ```

7. In the **PowerShell 7** window, type the following code to add Cody to Contoso_Sales using set variables, and then press **Enter**:

    ```powershell
    New-MgGroupMember -GroupId $group.Id -DirectoryObjectId $user.Id
    ```

8. In the **PowerShell 7** window, type the following code, and then press **Enter**:

    ```powershell
    Get-MgGroupMember -GroupId $group.Id | FL
    ```

9. Verify that you see **Cody Godinez** as value in **AdditionalProperties**.

10. Close PowerShell 7.

### Task 3: Review licenses and modify company branding

1. In the Microsoft Entra admin center, in the navigation pane, select **Billing** > **Licenses**.

2. On the **Licenses|Overview** page, under **Manage**, select **All products**.

   > Take note of the current licenses available and assigned for **Enterprise Mobility + Security E5** and **Office 365 E5**.

3. In the Microsoft Entra admin center, in the Navigation pane,under **Entra ID**, select **Custom branding**.

4. On the **Company Branding** page, under **Default sign-in experience**, select **Customize**.

5. On the **Customize default sign-in experience** page, navigate to the **Sign-in form** tab and configure the following settings:

   - Sign-in page text: **Contoso Corp. Sign-in Page**

6. Select **Review + Create**, review the settings and then select **Create**.

7. In the Microsoft Entra admin center, in the Navigation pane, select **Users**.

8. In the user list, select **Cody Godinez**.

9. In the Cody Godinez Profile page, under Manage, select **Licenses**.

   > Notice that Cody does not have any current license assignments. And that licensing must now be performed in the 365 Admin center.

10. Open a new tab in **Microsoft Edge**, in the address bar, enter **https://admin.microsoft.com**.

11. In the navigation pane on the left, select **Users** > **Active users**.

12. In the user list, select **Cody Godinez** (select the name, not the checkbox).

13. Select the **Licenses and apps** tab.

14. Select the check boxes next to **Enterprise Mobility + Security E5** and **Office 365 E5 (no Teams)**.

15. Select **Save changes**.

16. Once the changes have been saved, select the **X** in the upper-right corner to close the **Cody Godinez** pane. 

17. In the Microsoft 365 admin center, in the Navigation pane, select **Billing** > **Licenses**.

18. In the **Subscriptions** list, select **Enterprise Mobility + Security E5**.

19. Select the **Groups** tab, and then select **+ Assign licenses**.

20. Navigate into the **Enter a group name** textbox, and select the **Contoso_Managers** group.

21. Select **Assign Licenses**.

22. On the **You assigned licenses to Contoso_Managers** pane, select the **X** in the upper-right corner to close it.

23. In the upper-left corner of the **Enterprise Mobility + Security E5** page, select the **Back to licenses** link.

24. In the **Subscriptions** list, select **Office 365 E5 (no Teams)**.

25. Select the **Groups** tab, and then select **+ Assign licenses**.

26. Navigate into the **Enter a group name** textbox, and select the **Contoso_Managers** group.

27. Select **Assign Licenses**.

28. On the **You assigned licenses to Contoso_Managers** pane, select the **X** in the upper-right corner to close it.

29. In the Microsoft 365 admin center, in the Navigation pane, select **Billing** > **Licenses**.

30. In the **Subscriptions** list, select **Office 365 E5 (no Teams)**.

   > Take note of the users that are assigned the Office 365 E5 license. Edmund and Miranda both receive their license assignment from their membership in the Contoso_Managers group. You can select the **Groups** tab see if the licenses assigned correctly. It may take 3-5 minutes for the licenses to reprocess.

31. Close Microsoft Edge.

**Results**: After completing this exercise, you should have successfully created and managed groups, modified company branding, and assigned licenses.

**END OF LAB**
