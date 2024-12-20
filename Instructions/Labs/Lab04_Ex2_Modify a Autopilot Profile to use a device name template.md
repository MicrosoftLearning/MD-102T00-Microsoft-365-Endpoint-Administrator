# Practice Lab04: Manage Windows Autopilot

## Summary

In this lab, you will use Microsoft Intune to create and deploy a Windows Autopilot deployment profile.

## Exercise 2: Modify a Autopilot Profile to use a device name template

### Scenario

In order to identify devices enrolled with Autopilot more easily, you must establish a function to assign them a recognizable name.
The following specifications are required:

- The Windows Autopilot deployment profile must apply a device name template

### Task 1: Open the Windows autopilot deployment profile

1. Sign in to **MD102-WS1** as **Admin** with the password **Pa55w.rd**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Enrollment**. Make sure you are on the page for the Windows Operating System.

6. On the right side in the section **Windows Autopilot** select **Deployment profiles**.

7. Select **Contoso autopilot profile** Deployment Profile

8. Under **Mange** select **Properties** 

9. Select **Edit** in the section **Out-of-box experience (OOBE)** to modify the settings.

10. Turn on the settings **Apply device name template** by select **Yes** for this setting.

11. As you now see a new section has opend in this section you provide a template for the device name.

12. Type **Contoso-%SERIAL%** in the textbox for **Enter a name**.

13. As you now can see this. There are too many characters for the name template.

14. Delete the **-** behind **Contoso** to make the template fit.

15. Now a green checkmark is visible.

16. Select **Review + Save** to go to the review page.

17. Now select **Save** to save the changes you have made.

**Results**: After completing this exercise, you will have successfully opened and modified a Windows Autopilot deployment profile. The profile now use a device name template on the enrolled devices.

**END OF LAB**