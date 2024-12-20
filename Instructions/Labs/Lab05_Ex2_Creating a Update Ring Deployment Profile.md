# Practice Lab05: Manage Windows Updates

## Summary

In this lab, you will use Microsoft Intune to create profiles for Windows feature updates and for Windows quality updates.

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 2: Creating a Update Ring Deployment Profile

### Scenario

You need to manage quality updates for your Windows devices in a centralized and automated way.
The following specifications are required:

- Users need to be able to pause updates to suit their needs
- Users should be able to check for updates themselves
- Deadlines must be set to ensure updates are completed

### Task 1: Create a Update Ring Profile

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Devices**, then select **Windows**

6. Select **Windows Updates**, then select **Update rings**, then select **+Create Profile** to start the creation of a new Feature update deployment profile. 

7. Type **Windows Update Ring** in the Name.

8. Select **Next**.

9. View the settings and scroll down to the **Use deadline settings** section.

10. Select **Allow** on the deadline settings.

11. Type **10** in the Deadline for feature updates.

12. Type **5** in the Deadline for quality updates.

13. Select **Next**

14. On the next screen select **Add groups**, then search for the group **Windows Update Devices**.

15. Select the group, then select **Select** on the bottom of the page.

16. Select **Next**.

17. Review the settings you have made and select **Create** to create the Update ring.

### Taks 2: Verify the assignment in the Intune admin center

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. Select **Devices**, then select **Windows**.

6. Select **Windows updates**, then select **Update rings**

7. Select the update ring called **Windows Update Ring**.

8. In the overview you will see a short report of the status of all assigned devices.

9. Select **View report**.

10. It will take time for some information to show up here. When the data has been processed you will see the status of each device in here. 

**Results**: After completing this exercise, you will have successfully created and assigned a Windows Update Ring. Also you have the knowledge to check the status of the devices in the report. 

**END OF LAB**