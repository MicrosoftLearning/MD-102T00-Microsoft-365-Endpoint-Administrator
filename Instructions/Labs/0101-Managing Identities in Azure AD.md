# Practice Lab: Managing Identities in Azure AD

## WWL Tenants - Terms of Use

If you are being provided with a tenant as a part of an instructor-led training delivery, please note that the tenant is made available for the purpose of supporting the hands-on labs in the instructor-led training. 

Tenants should not be shared or used for purposes outside of hands-on labs. The tenant used in this course is a trial tenant and cannot be used or accessed after the class is over and are not eligible for extension. 

Tenants must not be converted to a paid subscription. Tenants obtained as a part of this course remain the property of Microsoft Corporation and we reserve the right to obtain access and repossess at any time.

## Summary

In this lab, you will use the Azure Active Directory admin center to create and modify users, assign administrative roles, create and modify groups, and manage license assignments in Azure AD.

## Exercise 1: Creating users in Azure AD

### Scenario

You need to create user accounts in Azure AD for new employees that will start next week. New users are listed in the following table:

| Name           | User Name                             | Password   | Job title        | Department |
| -------------- | ------------------------------------- | ---------- | ---------------- | ---------- |
| Edmund Reeve   | `ereeve@yourtenant.onmicrosoft.com`   | Pa55-w.rd! | HR Rep           | HR         |
| Miranda Snider | `msnider@yourtenant.onmicrosoft.com`  | Pa55-w.rd! | Helpdesk Manager | Operations |
| Cody Godinez   | `cgodinez@yourtenant.onmicrosoft.com` | Pa55-w.rd! | Sales Rep        | Sales      |

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

11. In the Navigation pane, under **Admin centers** select **Azure Active Directory**. The Microsoft Entra admin center opens.

12. In the Microsoft Entra admin center, in the navigation pane, select **Users**.

    > Take note of the users that already exist as members of the Azure AD domain. Each user is enabled as indicated on the **Account enabled** column. The **Directory synced** column states **No** for all current users. This indicates that each user was created directly in Azure AD and not synchronized from an on-premises directory service.

13. On the **Users | All users** page, select **New user** then select **Create new user**.

14. On the **New User** page, ensure that **Create user** is selected, enter the following:

    - User Principal Name: **`ereeve`**
    - Display Name: **Edmund Reeve**

15. Uncheck **Auto-generated password**

16. Next to **Password**, enter **Pa55-w.rd!**.

17. Select **Next:Properties** located at the bottom of the page.

18. Next to **Firt name**, enter **Edmund**.

19. Next to **Last name**, enter **Reeve**.

20. Next to **User type**, make note that **Member** is selected.
    > Note: The **Member** user type is the default user type. This user type is used for most users in an organization.

21. Next to **Job title**, enter **HR Rep**.

22. Next to **Department**, enter **HR**.

23. Next to **Usage location**, select **United States**.

24. Select **Next:Assignments** located at the bottom of the page.

25. On the **Assignments** page, note that no assignments are selected.
    > by default no groups are assigned to the user. This is because the user is not a member of any groups until you assign them.

26. Select **Next:Review + create** located at the bottom of the page.
    > Review the information on this page to ensure that it is correct.

27. Select **Create**.

28. On the **Users | All users** page, select **New user** then select **Create new user**.

29. On the **New User** page, ensure that **Create user** is selected, enter the following:

    - User Principal Name: **`msnider`**
    - Display Name: **Miranda Snider**

30. Uncheck **Auto-generated password**

31. Next to **Password**, enter **Pa55-w.rd!**.

32. Select **Next:Properties** located at the bottom of the page.

33. Next to **Firt name**, enter **Miranda**.

34. Next to **Last name**, enter **Snider**.

35. Next to **User type**, make note that **Member** is selected.

36. Next to **Job title**, enter **Helpdesk Manager**.

37. Next to **Department**, enter **Operations**.

38. Next to **Usage location**, select **United States**.

39. Select **Next:Assignments** located at the bottom of the page.

40. On the **Assignments** page, note that no assignments are selected.

41. Select **Next:Review + create** located at the bottom of the page.

42. Select **Create**.

43. Minimize the **Microsoft Edge** window.

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
New-MsolUser –UserPrincipalName cgodinez@yourtenant.onmicrosoft.com -DisplayName “Cody Godinez” -FirstName “Cody” -LastName “Godinez” -Password ‘Pa55-w.rd!’ -ForceChangePassword $false -UsageLocation “US” -Title "Sales Rep" -Department "Sales"
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

2. In the Microsoft Entra admin center, in the Navigation pane, select **Contoso|Overview**.

3. In the Navigation pane, select **Roles & administrators**.
    > Note that you can scroll down the list or use the search box to find the **Role** you are looking for.

4. Using the search box, search for **Global administrator**.

5. Select **Global administrator**.

6. In the **Global administrator** pane, select **Add assignments**.

7. In the **Add assignments** pane, select **Allan Deyoung**.

8. Select **Add**.

9. In the navigation pane, select **Roles & administrators | All roles**.

10. Using the search box, search for **User administrator**.

11. Select **User administrator**.

12. In the **User administrator** pane, select **Add assignments**.

13. In the **Add assignments** pane, search for and select **Edmund Reeve**.

14. Select **Add**.

15. In the navigation pane, select **Roles & administrators | All roles**.

16. Using the search box, search for **Helpdesk administrator**.

17. Select **Helpdesk administrator**.

18. In the **Helpdesk administrator** pane, select **Add assignments**.

19. In the **Add assignments** pane, search for and select **Miranda Snider**.

20. Select **Add**.

21. In the navigation pane, select **Home**.

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

1. On **SEA-SVR1**, in the Azure Active Directory admin center, in the navigation pane, select **Contoso|Overview**.

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

1. In the Azure Active Directory admin center, select **Home**. Then select **Azure Active Directory**.

2. On the **Contoso|Overview** page, under **Manage**, select **Licenses**.

3. On the **Licenses|Overview** page, under **Manage**, select **All products**.

   > Take note of the current licenses available and assigned for **Enterprise Mobility + Security E5** and **Office 365 E5**.

4. In the Azure Active Directory admin center, in the Navigation pane, select **Contoso | Licenses**.

5. On the **Contoso|Overview** page, under **Manage**, select **Company branding** and then select **Customize** under the **Default sign-in experience**.

6. On the Default sign-in experience page, navigate to the **Sign-in form** and configure the following settings and then select **Review + create**:

   - Sign-in page text: **Contoso Corp. Sign-in Page**

7. Review the settings and then select **Create**.

8. In the Azure Active Directory admin center, in the Navigation pane, select **Users**.

9. In the user list, select **Cody Godinez**.

10. In the Cody Godinez|Profile page, under Manage, select **Licenses**.

   > Notice that Cody does not have any current license assignments.

11. Select **Assignments**.

12. In the Update license assignments page, select the check box next to **Enterprise Mobility + Security E5** and **Office 365 E5**.

13. Select **Save**.

14. In the Azure Active Directory admin center, in the Navigation pane, select **Contoso | Overview**.

15. In the navigation pane, select **Groups**.

16. On the Groups|All groups page, select **Contoso_Managers**.

17. On the Contoso_Managers page, select **Licenses**.

    > Notice that the Contoso_Managers group does not have any current license assignments.

18. Select **Assignments**.

19. In the Update license assignments page, select the check box next to **Enterprise Mobility + Security E5** and **Office 365 E5**.

20. Select **Save**.

21. In the Azure Active Directory admin center, in the Navigation pane, select **Contoso|Overview**.

22. On the **Contoso|Overview** page, under **Manage**, select **Licenses**.

23. On the **Licenses|Overview** page, under **Manage**, select **All products**.

24. On the Licenses|All products page, select **Office 365 E5**.

   > Take note of the users that are assigned the Office 365 E5 license. Notice the Assignment Paths column which indicates how license assignment is configured for each user. Edmund and Miranda both receive their license assignment from their membership in the Contoso_Managers group. You may need to select **Refresh** a couple of times to update the Assignment path column.

25. Close Microsoft Edge.

**Results**: After completing this exercise, you should have successfully created and managed groups, modified company branding, and assigned licenses.

**END OF LAB**
