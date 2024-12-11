# Practice Lab02: Manage Windows Device Configuration
## Summary

In this lab, you will use Microsoft Intune to create and apply a Configuration profile for a Windows 11 device.

## Exercise 2: Modify an assigned Configuration profile policy  

### Scenario

There was an exception to Contoso's policy that specifies that members of the Developer department should not have the Privacy options blocked in Settings on their devices. This change should be implemented and tested.

### Task 1: Change settings in an assigned Configuration profile

1. Switch to **SEA-WS1**.

2. On **SEA-WS1**, in the Microsoft Intune admin center, select **Devices** and then select **Configuration**. 

3. On the **Devices | Configuration** page, in the **Policies** tab, select **Contoso Developer -  standard**.

4. On the **Contoso Developer -  standard** page, scroll down to the **Configuration settings** section, and then select **Edit**.

5. On the **Device restrictions** page, expand **Control Panel and Settings**. 

6. Next to **Privacy**, select **Not configured**. 

7. Select **Review + save**, and then select **Save**.

### Task 2: Force device synchronization from Intune Manager admin center

1. On **SEA-WS1**, in the Microsoft Intune admin center, select **Devices** in the navigation pane and then select **All devices**.
    
2. In the details pane, select **SEA-WS2**. 
    
3. On the **SEA-WS2** page, select **Sync** and when prompted select **Yes**. 

   _Note: Intune will contact the device and tell it to synchronize all policies. This may take up to 5 minutes._

4. Close Microsoft Edge.

### Task 3: Verify changes on SEA-WS2

1. Switch to **SEA-WS2**.

2. On **SEA-WS2** and on the taskbar, select **Start** and then select the **Settings** app.

3. In the **Settings** app, select **Privacy & security** and verify that all of the customization options are back.

4. Close all open windows and sign out of **SEA-WS2**.

**Results**: After completing this exercise, you will have successfully modified an assigned a Configuration profile, modified a Configuration profile, and verified the changes.

**END OF LAB**