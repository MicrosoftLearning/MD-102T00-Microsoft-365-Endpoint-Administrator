---
lab:
  title: 'Practice Lab 0305: Monitor device and user activity in Intune'
  description: In this lab, you will monitor user Sign-in activity, Audit logs, and device information.
  duration: 60 minutes
  level: 200
  islab: true
---

# Practice Lab 0305: Monitor device and user activity in Intune

## Summary

In this lab, you will monitor user Sign-in activity, Audit logs, and device information.

### Prerequisites

The following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing identities by using Entra Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Policies

  > [!NOTE]
  > You will also need a mobile phone that can receive text messages used to secure Windows Hello sign-in authentication to Microsoft Entra ID.

### Scenario

You need to review Aaron Nicholls' sign-in activity and general information provided by the Audit logs. You also need to verify the hardware on SEA-WS1 and confirm the configuration policy assigned to this device is successfully applied.

### Task 1: Monitor user activity

1. On **SEA-SVR1**, on the taskbar, select **Microsoft Edge**.

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**.

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. In the Microsoft Intune admin center, select **Users**.

5. In the **Users** navigation pane, select **Sign-in logs**.

6. In the **Users | Sign-in logs** page, where **User sign-ins (interactive)** activity is listed, select the first entry where the **User** column displays **Aaron Nicholls**.

7. In the **Activity Details: Sign-ins** pane, Aaron Nicholls' sign-in details are displayed.

8. Select each of the main tabs, including **Basic info**, **Location**, **Device info**, **Authentication Details**, and **Conditional Access**. Scroll to examine information on each tab and then select **X** in the top-right corner to close the **Activity Details** pane.

9. In the **Users** navigation pane, select **Audit logs**.

10. In the **Users | Audit logs** page, audit information is displayed about administrative changes to users. Examine the information by selecting the various entries.

### Task 2: Monitor device information

1. In the Microsoft Intune admin center, from the navigation pane, select **Devices**.

2. Select **All devices**, and in the details pane, select **SEA-WS1**. Information about the device such as name, primary user, and operating system is displayed.

3. In the **SEA-WS1** navigation pane, select **Hardware** and examine the hardware inventory.

4. In the **SEA-WS1** navigation pane, select **Discovered apps** and examine the app inventory.

5. In the **SEA-WS1** navigation pane, select **Device configuration**. In the details pane, take note of the device configuration policies assigned to the device. The **State** column should display **Succeeded**, which means that the profiles are applied successfully to the device.

6. In the details pane, select **Contoso Developer - standard**.

7. On the **SEA-WS1 - Profile Settings** page, take note of each setting you configured in the policy.

   > The **Setting status** column should display **Succeeded** for all settings.

8. In the Microsoft Intune admin center, from the navigation pane, select **Home**.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you have successfully monitored user sign-in activity, audit logs, and device information.

**END OF LAB**
