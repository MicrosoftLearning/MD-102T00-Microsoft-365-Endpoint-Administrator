# Practice Lab03: Manage Windows Device Compliance

## Summary

In this lab, you validate device compliance by configuring a compliance policy and associated conditional access rule used to determine the status of a managed device. 

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Entra ID

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0301-Creating and Deploying Configuration Profiles

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

## Exercise 1: Configuring compliance policies 

### Scenario

Contoso would like to ensure that Windows devices that are enrolled in Intune meet a minimum configuration specification. The following are specifications are required:

- Minimum Windows operating system version: 10.0.19041.329
- Microsoft Defender Antimalware required

If a device meets these requirements, it will be marked as compliant. If the device does not meet these requirements, the device should be marked as non-compliant.

### Task 1: Create and assign a compliance policy

1. Sign in to **SEA-SVR1** as **Contoso\\Administrator** with the password **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**. 

4. Sign in as as **`admin@yourtenant.onmicrosoft.com`** with the default tenant password.

5. From the navigation pane select **Devices**, then select **Compliance**.

6. On the **Devices | Compliance** blade, in the details pane select **Create policy**.

7. On the **Create a policy** blade, provide the following value and select **Create**:

    - Platform: **Windows 10 and later**

8. On the **Basics** tab, provide the following value and select **Next**:

    - Name: **Compliance1**

9. On the **Compliance settings** tab, expand **Device Health** and review the available settings.

10. On the **Compliance settings** tab, expand **Device Properties**. In the **Minimum OS version**
    field, type **10.0.19041.329**.

11. On the **Compliance settings** tab, expand **System Security**. Set the **Microsoft Defender Antimalware** setting to **Require**. 

12. Select **Next**. On the **Actions for noncompliance** tab, note the action to **Mark device noncompliant** default setting is **immediately**. 

    > Review how you can configure the number of days after which the device is marked as noncompliant, and configuration additional actions. 

13. Select **Next**. On the **Assignments** tab, under **Included groups** select **Add groups**. Select **Windows Devices**, choose **Select**, and then select **Next**. 

    _Note: The **Windows Devices** group was created in the Module 0301 lab._

14. On the **Review + create** tab, review the settings and then select **Create**.

15. In the navigation menu, select **Devices** and then in the Devices navigation pane, select **Compliance**.

16. On the **Devices | Compliance** blade, select the **Compliance settings** tab.

17. On the **Compliance settings** page, toggle **Mark devices with no compliance policy assigned as** so it reads **Not compliant** and then select **Save**. 

    > This setting will ensure that any device that does not have a compliance policy assigned will be set to **Not compliant**.

**Results**: After completing this exercise, you will have successfully configured a compliance policy.


**END OF LAB**
