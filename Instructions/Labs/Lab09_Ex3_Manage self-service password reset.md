# Practice Lab09: Manage User & Device Security in Entra & Intune

## Summary

In this lab, you will configure and validate self-service password reset (SSPR) for user accounts in Entra ID.

### Prerequisites

### Exercise 4: Manage self-service password reset

### Scenario

The Help Desk has indicated that a large number of support tickets are related to password resets. You have been asked to propose a solution for users to reset their own password. 

### Task 1: Enable self-service password reset

1. On **SEA-WS1**, on the taskbar select **Microsoft Edge**, in the address bar type **https://entra.microsoft.com/**, and then press **Enter**.

2. Sign in as **`Admin@yourtenant.onmicrosoft.com`**, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**. 

   > The Microsoft Entra admin center opens.

3. In the Microsoft Entra admin center, Navigate to the Search resources section of the site.

4. In the search box, type **password reset**, and then select **Password reset**.

5. In the **Password reset | Properties** window, select **All** to enable self-service password reset to all users. Select **Save**.

6. On the **Password reset | Properties** blade, select **Authentication methods**.

7. For the methods available to users, ensure that **Mobile Phone** and **Email** are selected, and then select **Security Questions**.

8. For the **Number of questions required to register**, select **3**.

9. For the **Number of questions required to reset**, select **3**.

10. In the **Select security questions** section, select **No security questions configured**, then select **Predefined**. Select three questions of your choice, and then select **Ok** twice.

11. Select **Save**.

12. Select **Registration** Select **No** for **Require users to register when signing in**, and the select **Save**.

15. Close Microsoft Edge.

### Task 2: Validate self-service password reset

1. Switch to **SEA-WS2**.

2. If necessary, sign in as **Admin** with the password of **Pa55w.rd**.

3. On the taskbar, select **Microsoft Edge**.

4. Browse to **https://myaccount.microsoft.com**. 

5. On the **Pick an account** page, select **Use another account**.

6. On the **Sign in** page, sign in as **`DiegoS@yourtenant.onmicrosoft.com`**.

7. On the **My Account** page, in the navigation pane, select **Password**.

8. On the **Change password** page, enter the following information and then select **submit**:
     - Old password: **Enter User password** 
     - Create new password: **Pa55w.rd1234!**
     - Confirm new password: **Pa55w.rd1234!**

9.  If Microsoft Edge prompts to save the password, select **Save**.

10. Close Microsoft Edge and sign out of SEA-WS2.

**Results**: After completing this exercise, you will have successfully configured and validated self-service password reset.

**END OF LAB**
