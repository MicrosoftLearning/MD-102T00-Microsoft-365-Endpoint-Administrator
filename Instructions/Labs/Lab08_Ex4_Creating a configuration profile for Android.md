# Practice Lab08: Manage Mobile Devices

## Summary

### Prerequisites

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Entra ID.

### Exercise 4: Deploy apps and create a configuration profile for Android

### Scenario

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

1. Select **Microsoft 365 (offiec)** from the list.

1. On the details pageof the applicytion, select **Select** and then on the upper left side, select **Sync**

>Note:  It takes some time until the app is shown on the **Android | Android apps** page.

13. On the **Android | Android apps** page, select **Refresh** and select **Microsoft 365 (Office)**.

1. On the **Microsoft 365 (Office)** page, under **Manage**, select **Properties**.

1. On the **Microsoft 365 (Office) | Properties** page, select **Edit** next to **Assignment**.

1. In the **Assignments** tab, under **Required**, select **+ Add group**.

1. On the **Select groups** blade, enter the following group **Prod_Intune_Android Fully Managed User Devices_Marketing**, then select the listed group and select **Select**.

1. In the **Assignments** tab, select **Review + save**.

1. In the **Review + save** tab, select **Save**.

### Task 2