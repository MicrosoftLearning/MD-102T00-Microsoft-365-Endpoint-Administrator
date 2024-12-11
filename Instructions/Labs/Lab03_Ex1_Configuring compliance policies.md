# Practice Lab03: Manage Windows Device Compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

## Exercise 1: Configuring compliance policies 

### Scenario

Contoso would like to ensure that Windows devices that are enrolled in Intune meet a minimum configuration specification. The following are specifications are required:

- Minimum Windows operating system version: 10.0.19041.329
- Microsoft Defender Antimalware required

If a device meets these requirements, it will be marked as compliant. If the device does not meet these requirements, the device should be marked as non-compliant.

### Task 1: Create a dynamic Entra ID device group

Sign in to **SEA-WS1** as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

1. On the taskbar, select **Microsoft Edge**.

1. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

1. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

1. In the Microsoft Intune admin center, in the navigation pane, select **Groups**.

1. On the **Groups | Overview** page, select **All groups**.

1. On the **Groups | All Groups** page, on the details pane, select **New group**.

2. On the **Group** blade, provide the following values:

   - Group type: **Security**
   - Group name: **Windows Devices**
   - Membership type: **Dynamic Device**

3. Under the **Dynamic Device Members** section, select **Add dynamic query**. 

4. On the **Dynamic membership rules** blade, in the **Rule syntax** section, select **Edit**. 
    
5. In the **Edit rule syntax** text box, add the following simple membership rule and select **OK**.

```
(device.deviceOSType -contains "Windows")
```

6. On the **Dynamic membership rules** blade, select **Save**.

7. On the **New Group** page, select **Create**.

### Task 2: Create and assign a compliance policy

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**, then select **Compliance**.

1. On the **Devices | Compliance** page, in the **Policies** tab, select **Create policy**.

1. On the **Create a policy** blade, provide the following value and select **Create**:

    - Platform: **Windows 10 and later**

1. In the **Basics** tab, enter the following information and select **Next**:

    - Name: **Compliance1**

1. In the **Compliance settings** tab, expand **Device Health** and review the available settings.

1. In the **Compliance settings** tab, expand **Device Properties**, then type **10.0.19045.4529** in the text box next to  **Minimum OS version**.

1. In the **Compliance settings** tab, expand **System Security**, then select **Require** next to **Microsoft Defender Antimalware** and then select **Next**.

1. In the **Actions for noncompliance** tab, note the action to **Mark device noncompliant** default setting is **immediately** and then select **Next**.

    > Review how you can configure the number of days after which the device is marked as noncompliant, and configuration additional actions. 

1. In the **Assignments** tab, under **Included groups** select **Add groups**, then select **Windows Devices**, then select **Select**, and then select **Next**. 

1. In the **Review + create** tab, review the settings and then select **Create**.

1. In the left navigation pane, select **Devices**.

1. On the **Devices | Overview** page, under **Manage devices**, select **Compliance**. 

1. On the **Devices | Compliance** page, select the **Compliance settings** tab.

1. On the **Compliance settings** page, toggle **Mark devices with no compliance policy assigned as** so it reads **Not compliant** and then select **Save**. 

    > This setting will ensure that any device that does not have a compliance policy assigned will be set to **Not compliant**.

**Results**: After completing this exercise, you will have successfully configured a compliance policy.

**END OF LAB**
