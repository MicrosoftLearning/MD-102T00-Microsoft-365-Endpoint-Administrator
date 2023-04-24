# Practice Lab: Managing Identities in Azure AD

## Summary

In this lab, you will use the Azure Active Directory admin center to create and modify users, assign administrative roles, create and modify groups, and manage license assignments in Azure AD.

## Exercise 1: Creating users in Azure AD

### Scenario

You need to create user accounts in Azure AD for new employees that will start next week. New users are listed in the following table:

| Name           | User Name                             | Password | Job title        | Department |
| -------------- | ------------------------------------- | -------- | ---------------- | ---------- |
| Edmund Reeve   | `ereeve@yourtenant.onmicrosoft.com`   | Pa55w.rd | HR Rep           | HR         |
| Miranda Snider | `msnider@yourtenant.onmicrosoft.com`  | Pa55w.rd | Helpdesk Manager | Operations |
| Cody Godinez   | `cgodinez@yourtenant.onmicrosoft.com` | Pa55w.rd | Sales Rep        | Sales      |

_Note: For location use either your local region or United States._

You've also been told that several more employees will be hired over the next couple of months. You've decided that scripting would be a far more efficient method of adding a large number of new users. You've decided to create a PowerShell script and test it out when you create Cody Godinez's account.

### Task 1: Create users by using the Azure Active Directory admin center

1. On **SEA-SVR1**, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd**.

2. Close **Server Manager**.

3. On the taskbar, select **Microsoft Edge**.

4. In the address bar, enter **<http://portal.office.com>**.

5. At the Sign-in prompt, enter **`admin@yourtenant.onmicrosoft.com`** and then select **Next**.

6. At the Enter password page, enter the password for the Admin account and then select **Sign in**.

   > Note: Check with your instructor on the password to use for signing in with the Admin account.

7. At the Save password prompt, select **Save**.

8. At the Stay signed in prompt, select **No**. The Office 365 portal opens.

9. At the top left corner, select the **App launcher** and then select **Admin**. The Microsoft 365 admin center opens.

10. Select the **Navigation menu** and then select **Show all**.

11. In the Navigation pane, under **Admin centers** select **Azure Active Directory**. The Azure Active Directory admin center opens.

12. In the Azure Active Directory admin center, in the navigation pane, select **Users**.

    > Take note of the users that already exist as members of the Azure AD domain. Each user is enabled as indicated on the **Account enabled** column. The **Directory synced** column states **No** for all current users. This indicates that each user was created directly in Azure AD and not synchronized from an on-premises directory service.

13. On the **Users | All users** page, select **New user** then select **Create new user**.

14. On the **New User** page, ensure that **Create user** is selected, enter the following:

    - User Name: **`ereeve@yourtenant.onmicrosoft.com`**
    - Name: **Edmund Reeve**

15. Select **Let me create the password.**

16. Next to **Initial password**, enter **Pa55w.rd**.

17. Under **Groups and roles**, take note that this new user will not be a member of any group, and will be assigned the **User** role.

    > Note: The **User** role does not provide any administrative privileges

18. Under **Settings**, next to **Usage location**, select **United States**. If necessary, close the **Save password** prompt.

19. Under **Job info**, next to **Job title**, enter **HR Rep**.

20. Under **Job info**, next to **Department**, enter **HR** and then select **Create**.

21. On the **Users | All users** page, select **New user** then select **Create New User**.

22. On the **New User** page, ensure that **Create user** is selected, enter the following:

    - User Name: **`msnider@yourtenant.onmicrosoft.com`**
    - Name: **Miranda Snider**

23. Select **Let me create the password.**

24. Next to **Initial password**, enter **Pa55w.rd**.

25. Under **Groups and roles**, take note that this new user will not be a member of any group, and will be assigned the **User** role.

    > Note: The **User** role does not provide any administrative privileges.

26. Under **Settings**, next to **Usage location**, select **United States**. If necessary, close the **Save password** prompt.

27. Under **Job info**, next to **Job title**, enter **Helpdesk Manager**.

28. Under **Job info**, next to **Department**, enter **Operations** and then select **Create**.

### Task 2: Create users by using PowerShell

1. On **SEA-SVR1**, on the taskbar, right-click **Start**, and then select **Windows PowerShell (Admin)**.

2. In the **Windows PowerShell** window, type the following command, and then press **Enter**. If prompted, enter **Y** at the NuGet and repository messages:

```
Install-Module MSOnline
```

3. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Connect-MsolService
```

4. In the **Sign in to your account** dialog box, sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant password, and then select **Sign in**.

5. In the **Windows PowerShell** window, type the following code to create a new user, and then press **Enter**. Be sure to replace "yourtenant" with your assigned tenant name:

```
New-MsolUser –UserPrincipalName cgodinez@yourtenant.onmicrosoft.com -DisplayName “Cody Godinez” -FirstName “Cody” -LastName “Godinez” -Password ‘Pa55w.rd’ -ForceChangePassword $false -UsageLocation “US” -Title "Sales Rep" -Department "Sales"
```

6. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Get-MsolUser
```

> Verify that the list of users from your tenant is displayed. Also take note of which users have a license assigned. Any user with the **isLicensed** value of **False** has not been assigned a license.

**Results**: After completing this exercise, you will have successfully created new user accounts in Azure AD.

## Exercise 2: Assigning Administrative Roles in Azure AD

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

2. In the Azure Active Directory admin center, in the Navigation pane, select **Azure Active Directory**.

3. On the **Contoso|Overview** page, under **Manage**, select **Roles and administrators**.

   > Take note of the various administrative roles available in Azure AD.

4. On the **Contoso|Roles and administrators** page, select **Global administrator**. Ensure that **Assignments** is selected.

   > Take note of the users that currently are assigned the Global administrator role. Isaiah Langer, Megan Bowan, and Nestor Wilke should not be assigned Global administrator privileges. Allan Deyoung needs to be assigned the Global administrator role.

5. On the **Global administrator|Assignments** page, select the check box next to **Isaiah Langer**, **Megan Bowen**, and **Nestor Wilke** and then select **Remove assignments**. Select **Yes** at the message prompt.

6. On the **Global administrator|Assignments** page, select **Add assignments**.

7. On the Add assignments page, select **Allan Deyoung** and then select **Add**.

8. At the top of the page, in the navigation link, select **Contoso**.

9. On the **Contoso|Roles and administrators** page, select **User administrator**. Ensure that **Assignments** is selected.

   > Notice that there are no users currently assigned to the User administrator role.

10. On the **User administrator|Assignments** page, select **Add assignments**.

11. On the Add assignments page, select **Edmund Reeve** and then select **Add**.

12. At the top of the page, in the navigation link, select **Contoso**.

13. On the **Contoso|Roles and administrators** page, select **Helpdesk administrator**. Ensure that **Assignments** is selected.

    > Notice that there are no users currently assigned to the Helpdesk administrator role.

14. On the **User administrator|Assignments** page, select **Add assignments**.

15. On the Add assignments page, select **Miranda Snider** and then select **Add**.

16. At the top of the page, in the navigation link, select **Contoso**.

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

### Task 1: Create groups by using the Azure Active Directory admin center

1. On **SEA-SVR1**, in the Azure Active Directory admin center, in the navigation pane, select **Azure Active Directory**.

2. On the **Contoso|Overview** page, under **Manage**, select **Groups**.

3. Select **New group**.

4. On the **New Group** page, enter the following:

    - Group type: **Security**
    - Group name: **Contoso_Managers**
    - Membership type: **Assigned**

5. Under Members, select **No members selected**.

6. In the Add members page add **Edmund Reeve**, **Miranda Snider**, and then click **Select**.

7. Select **Create**.

### Task 2: Create groups by using PowerShell

1. On SEA-SVR1, switch to Windows PowerShell.

2. In the **Windows PowerShell** window, type the following code to create a new group, and then press **Enter**:

```
New-MsolGroup -DisplayName “Contoso_Sales” -Description “Contoso Sales team users”
```

3. In the **Windows PowerShell** window, type the following command, and then press **Enter**:

```
Get-MsolGroup
```

4. Verify that you get the list of groups in your tenant, including the Contoso_Sales group you just created.

5. In the **Windows PowerShell** window, type the following code to define a variable as the Contoso_Sales group, and then press
    **Enter**:

```
$group = Get-MsolGroup | Where-Object {$_.DisplayName -eq "Contoso_Sales"}
```

6. In the **Windows PowerShell** window, type the following code to define another variable as the user, and then press
    **Enter**:

```
$user = Get-MsolUser | Where-Object {$_.DisplayName -eq “Cody Godinez”}
```

7. In the **Windows PowerShell** window, type the following code to add Cody to Contoso_Sales using set variables, and then press **Enter**:

```
Add-MsolGroupMember -GroupObjectId $group.ObjectId -GroupMemberType "User" -GroupMemberObjectId $user.ObjectId
```

8. In the **Windows PowerShell** window, type the following code, and then press **Enter**:

```
Get-MsolGroupMember -GroupObjectId $group.ObjectId

```

9. Verify that you get **Cody Godinez** as a result.

10. Close Windows PowerShell.

### Task 3: Review licenses and modify company branding

1. In the Azure Active Directory admin center, in the Navigation pane, select **Azure Active Directory**.

2. On the **Contoso|Overview** page, under **Manage**, select **Licenses**.

3. On the **Licenses|Overview** page, under **Manage**, select **All products**.

   > Take note of the current licenses available and assigned for **Enterprise Mobility + Security E5** and **Office 365 E5**.

4. In the Azure Active Directory admin center, in the Navigation pane, select **Azure Active Directory**.

5. On the **Contoso|Overview** page, under **Manage**, select **Company branding** and then select **Configure**.

6. On the Configure company branding page, configure the following settings and then select **Save**:

   - Sign-in page text: **Contoso Corp. Sign-in Page**
   - Show option to remain signed in: **Selected**

7. In the Azure Active Directory admin center, in the Navigation pane, select **Users**.

8. In the user list, select **Cody Godinez**.

9. In the Cody Godinez|Profile page, under Manage, select **Licenses**.

   > Notice that Cody does not have any current license assignments.

10. Select **Assignments**.

11. In the Update license assignments page, select the check box next to **Enterprise Mobility + Security E5** and **Office 365 E5**.

12. Select **Save**.

13. In the Azure Active Directory admin center, in the Navigation pane, select **Azure Active Directory**.

14. In the navigation pane, select **Groups**.

15. On the Groups|All groups page, select **Contoso_Managers**.

16. On the Contoso_Managers page, select **Licenses**.

    > Notice that the Contoso_Managers group does not have any current license assignments.

17. Select **Assignments**.

18. In the Update license assignments page, select the check box next to **Enterprise Mobility + Security E5** and **Office 365 E5**.

19. Select **Save**.

20. In the Azure Active Directory admin center, in the Navigation pane, select **Azure Active Directory**.

21. On the **Contoso|Overview** page, under **Manage**, select **Licenses**.

22. On the **Licenses|Overview** page, under **Manage**, select **All products**.

23. On the Licenses|All products page, select **Office 365 E5**.

   > Take note of the users that are assigned the Office 365 E5 license. Notice the Assignment Paths column which indicates how license assignment is configured for each user. Edmund and Miranda both receive their license assignment from their membership in the Contoso_Managers group. You may need to select **Refresh** a couple of times to update the Assignment path column.

24. Close Microsoft Edge.

**Results**: After completing this exercise, you should have successfully created and managed groups, modified company branding, and assigned licenses.

**END OF LAB**
