# Practice Lab08: Manage Mobile Devices

## Summary

In this lab, you deploy apps and configure Android devices.

### Exercise 4: Deploy apps and create a configuration profile for Android

### Scenario

Your organization is rolling out fully managed Android devices to the Marketing department to enhance productivity and ensure secure access to company resources. As an Intune administrator, you are tasked with deploying the Microsoft 365 (Office) app to these devices and configuring device restriction policies tailored to the department's requirements.

### Task 1: Deploy apps to android devices

1. Sign in to **SEA-WS3** as **Admin** with the password **Pa55w.rd**. 

1. On the taskbar, select **Microsoft Edge**.

1. In Microsoft Edge, type **https://intune.microsoft.com** in the  address bar, and then press **Enter**.

1. Sign in as user `Admin@yourtenant.onmicrosoft.com`, and use the tenant Admin password. If the **Stay signed in?** prompt appears, select **No**.

1. In the Microsoft Intune admin center, in the left navigation pane select **Apps**.

1. On the **Apps | Overview** page, select **Android**.

1. On the **Android | Android apps** page, select **+ Add**.

1. On the **Select app type**, select **Managed Google Play app** as app type and select **Select**.

1. If the **This site uses cookis** prompt appears, select **Got it**.

1. On the **Managed Google Play** page, in the search box, enter **Microsoft 365** and select the search button.

1. Select **Microsoft 365 (office)** from the list.

1. On the details pageof the applicytion, select **Select** and then on the upper left side, select **Sync**

>Note:  It takes some time until the app is shown on the **Android | Android apps** page.

13. On the **Android | Android apps** page, select **Refresh** and select **Microsoft 365 (Office)**.

1. On the **Microsoft 365 (Office)** page, under **Manage**, select **Properties**.

1. On the **Microsoft 365 (Office) | Properties** page, select **Edit** next to **Assignment**.

1. In the **Assignments** tab, under **Required**, select **+ Add group**.

1. On the **Select groups** blade, in the search field, enter the following group **Prod_Intune_Android Fully Managed User Devices_Marketing**, then select the listed group and select **Select**.

1. In the **Assignments** tab, select **Review + save**.

1. In the **Review + save** tab, select **Save**.

### Task 2 Create a configuration profile based on scenario requirements

1. In the Microsoft Intune admin center, in the left navigation pane select **Devices**.

1. On the **Devices | Overview** page, under **Manage devices**, select **Configuration**.

1. On the **Devices | Configuration** page, in the **Policies** tab, select **+ Create** and then select **+ New Policy**.

1. In the **Create a profile** blade, select the following options and then select **Create**:

  - Platform: **Android Enterprise**
  - Profile type: **Device restrictions** under **Fully Managed, Dedicated, and Corporate-Owned Work Profile

5. In the **Basics** tab enter the following information and select **Next**:

  - Name: **Prod_Marketing_ Android Enterprise_Fully Managed_Device Restriction profile**
  - Description: **This Intune profile is designed for fully managed Android Enterprise devices used by the Marketing department in the Production environment. The profile enforces specific device restriction policies**

6. In the **Configuration settings** tab, expand **General** and then configure the following option:

  - System update: **Maintenance window**
  - Start time: **7:00 PM**
  - End time: **5:00 AM**

7. Expand **System security** and select **Require** next **Threat scan on apps** if not already selected.

1. Expand **Power Settings** and select **1 Minute** next to **Time to lock screen (work profile-level)**.

1. In the **Basics** tab, select **Next**.

1. In the **Scope tags** tab, select **Next**.

1. In the **Assignments** tab, select **Add groups**

1. On the **Select groups** blade, in the search field, enter the following group **Prod_Intune_Android Fully Managed User Devices_Marketing**, then select the listed group and select **Select**.

1. In the **Assignments** tab, select **Next**.

1. In the **Review + create** tab, select **Create**.

**END OF LAB**