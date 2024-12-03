# Practice Lab02: Manage Windows Device Configuration
## Summary

In this lab, you will use Microsoft Intune to create and apply a Configuration profile for a Windows 11 device.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.
## Exercise 2: Modify an assigned Configuration profile policy  

### Scenario

There was an exception to Contoso's policy that specifies that members of the Developer department should not have the Privacy options blocked in Settings on their devices. This change should be implemented and tested.

### Task 1: Change settings in an assigned Configuration profile

1. Switch to **SEA-SVR1**.

2. On **SEA-SVR1**, in the Microsoft Intune admin center, select **Devices** and then select **Configuration**. 

3. On the **Devices | Configuration** blade, in the details pane select **Contoso Developer -  standard**.

4. On the **Contoso Developer - standard** blade, scroll down to the **Configuration settings** section, and then select **Edit**.

5. On the **Device restrictions** page, expand **Control Panel and Settings**. 

6. Next to **Privacy**, select **Not configured**. 

7. Select **Review + save**, and then select **Save**.

### Task 2: Force device synchronization from Intune Manager admin center

1. On **SEA-SVR1**, in the Microsoft Intune admin center, select **Devices** in the navigation pane and then select **All devices**.
    
2. In the details pane, select **SEA-WS1**. 
    
3. On the **SEA-WS1** blade, select **Sync** and when prompted select **Yes**. 

   _Note: Intune will contact the device and tell it to synchronize all policies. This may take up to 5 minutes._

4. Close Microsoft Edge.

### Task 3: Verify changes on SEA-WS1

1. Switch to **SEA-WS1**.

2. On **SEA-WS1** and on the taskbar, select **Start** and then select the **Settings** app.

3. In the **Settings** app, select **Privacy & security** and verify that all of the customization options are back.

4. Close all open windows and sign out of **SEA-WS1**.

**Results**: After completing this exercise, you will have successfully modified an assigned a Configuration profile, modified a Configuration profile, and verified the changes.

**END OF LAB**