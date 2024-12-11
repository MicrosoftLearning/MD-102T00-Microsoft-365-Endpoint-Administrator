# Practice Lab04: Manage Windows Autopilot

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Create a Autopilot profile

### Scenario

You need to use a Windows Autopilot deployment profile to enroll Windows devices into your tenant.
The following are specifications are required:

- The enrollment needs to be User-Driven
- The devices needs to join Microsoft Entra ID
- No License Terms, privacy settings and account options should be visible for the user
- The user is not allowed to have local admin rights

### Task 1: Create a Autopilot Profile

1. Sign in to **SEA-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Enrollment**. Make sure you are on the page for the Windows Operating System.

6. On the right side in the section **Windows Autopilot** select **Deployment profiles**.

7. Select **+ Create profile** and then select **Windows PC**.

8. Fill in the Name as you like and add a description if you want. 

9. Make sure the **Convert all targeted devices to Autopilot** is switched to **No**.

10. Select **Next** on the bottom of the page.

### Task 2: Modify the OOBE Settings

1. In the section **Out-of-box experience (OOBW)** leave everything as it is and select **Next** on the bottom of the page.

2. In the section **Scope tags** leave everything as it is and select **Next** on the bottom of the page.

3. In the section **Assignments** you could assign groups to include or exclude. For now leave it empty and select **Next** on the bottom of the page. 

4. In the last section **Review + Create** go over all your settings and make sure they are like you want them to be. 

5. When everything is set up correct select **Create** and create the Windows Autopilot deployment profile.

### Task 3: Modify MDM user scope

1. From the navigation pane select **Devices**, then select **Enrollment**. Make sure you are on the page for the Windows Operating System.

2. Select **Automatic Enrollemnt** in the Section **Enrollment options**

3. Make sure the setting **All** is set for the MDM user scope.

4. Everything else we will leave as it is. 

5. Select **Save** to save your changes.

**Results**: After completing this exercise, you will have successfully created a Windows Autopilot deployment profile and modified the Automatic Enrollment to enroll windows devices into your tenant.

**END OF LAB**