# Practice Lab09: Manage User & Device Security in Entra & Intune

## Summary

In this lab, you will monitor user Sign-in activity, Audit logs, and device activity.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

### Exercise 1: Monitor device and user activity in Intune

### Scenario

You need to review Aaron Nicholls sign-in activity and general information provided by the Audit logs.  You also need to verify the hardware on SEA-WS1 and confirm the configuration profile assigned to this device is successfully applied.

### Task 1: Monitor user activity

1. On **SEA-WS1**, on the taskbar, select **Microsoft Edge**.

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. On the **Microsoft Intune admin center** page, select **Users**.

5. On the **Users|All users** pane, select **Sign-ins logs**.

6. In the Details pane, user sign-ins are listed. Select the first entry where the **User** column displays **Aaron Nicholls**.

7. In the **Details** pane, Aaron Nicholls´sign-in details are displayed.

8. Select each of the main pages, including **Basic info**, **Location**, **Device info**, **Authentication Details**, and **Conditional Access**. Scroll to examine information on each page and then select **X** in the top right hand corner to close out of the **Activity Details** page.

9. In the Users navigation pane, select **Audit logs**.

10. In the details pane, audit information is displayed about administrative changes to users. Examine the information by selecting the various entries.

**Results**: After completing this exercise, you will have successfully monitored user Sign-in activity, Audit logs, and device activity.

**END OF LAB**
