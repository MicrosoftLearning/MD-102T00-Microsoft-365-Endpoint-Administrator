# Practice Lab: Creating device inventory reports

## Summary

In this lab, you will view device inventory within Intune, Excel, and using Power BI.

### Prerequisites

To following lab(s) must be completed before this lab:

- 0101-Managing Identities in Azure AD

- 0102-Synchronizing Identities by using Azure AD Connect

- 0203-Manage Device Enrollment into Intune

- 0204-Enrolling devices into Intune

- 0403-Deploy Apps using Endpoint Configuration Manager

  > Note: You will also need a mobile phone that can receive text messages used to secure Windows Hello sign in authentication to Azure AD.

## Exercise 1: Reviewing device inventory with Intune 

### Scenario

You've been asked to review the inventory for SEA-WS1. Use Intune to review the devices hardware and app inventory.

### Task 1: Examining device inventory

1. On **SEA-SVR1**, if necessary, sign in as **Contoso\\Administrator** with the password of **Pa55w.rd** and close **Server Manager**.

2. On the taskbar, select **Microsoft Edge**.

3. In Microsoft Edge, type **https://endpoint.microsoft.com** in the address bar, and then press **Enter**. 

4. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

5. In the Microsoft Endpoint Manager admin center, select **Devices** from the navigation bar.

6. In the Devices navigation pane, select **All devices** and in the details pane, select the **SEA-WS1** entry. 

   > Examine the various information displayed about the device.

7. Select **Properties** and note that you can change the **Management name**, **Device category** and **Device ownership**.

8. In the **Management name** field, replace the existing text with **SEA-WS1** and select **Save**.

9. Under **Monitor**, select **Hardware** and examine the hardware from **SEA-WS1**. You need to scroll down to see it all.

10. Under **Monitor**, select **Discovered apps** and examine the app inventory from **SEA-WS1**. You may need to scroll down to see it all.

**Results**: After completing this exercise, you will have successfully reviewed device hardware and app inventory.

## Exercise 2: Exporting Intune data

### Scenario

Management is requesting a report of all devices. They do not have access to the Intune dashboards, and have requested the information be sent in a .csv file.

### Task 1: Export Intune Data

1. On **SEA-SVR1**, in the Microsoft Endpoint Manager admin center, select **Devices** and then select **All devices**.

2. On the **Devices | All devices** blade, in the details pane, select **Export**.

3. At the Export data for all managed devices message, select **Include all inventory data in the exported file**, and then select **Yes**.

   > Wait for the export to be prepared and a message that indicates that the export is complete.

4. At the top of the Microsoft Edge window, next to Downloads, select **Open downloads folder**.

5. In the Downloads folder, right-click the downloaded zip file and select **Extract all**. Browse to the **Downloads** folder and select **Extract**.

### Task 2: Review the exported Intune data

1. On **SEA-SVR1**, if necessary, browse to the Downloads folder.

2. Double-click the extracted .CSV file.

3. At the **How do you want to open this file** prompt, select **Notepad**, and then select **OK**.

4. Review the .CSV content. When finished, close Notepad.

5. Close all open Windows.

**Results**: After completing this exercise, you will have successfully exported Intune data for review.

## Exercise 3: Reviewing Intune Data using Power BI 

### Scenario

Your organization uses Power BI for reporting. You need to set up Power BI on SEA-CL1 and connect to the Intune Data Warehouse. You need to see a report that shows the primary user of each device. 

*Note: Power BI Desktop was deployed and installed using Configuration Manager in Module 4 lab 0403.*

### Task 1: Connect Power BI to the Intune Data Warehouse

1. Sign in to **SEA-CL1** as **Contoso\Administrator** with the password of **Pa55w.rd**.

2. Open Microsoft Edge, type **https://endpoint.microsoft.com** in the address bar, and then press **Enter**. 

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. In the Microsoft Endpoint Manager admin center, select **Reports** and then select **Data warehouse**.

5. In the **OData feed for reporting service** field, copy the Odata URL to the clipboard.

6. On SEA-CL1, on the desktop, double-click **Power BI Desktop**. Close all welcome pages.

7. After Power BI loads, with the **Home** tab selected in the ribbon, select the **Get Data** drop down arrow.

8. In the **Common data sources** list, select **OData feed**.

9. In the OData feed dialog box, paste the **OData URL** into the **URL** box and select **OK**.

10. In the **OData feed** dialog box, select the **Organizational account** tab and then select **Sign in**.

11. On the **Sign in** page, enter **`admin@yourtenant.onmicrosoft.com`** and select **Next**.

12. On the **Enter password** page, enter the tenant Admin password, and select **Sign in**.

13. Back on the **OData feed** dialog box, select **Connect**. Wait for the connection and load of data. The **Navigator** window opens.

14. In the **Navigator** window, select all tables. You can select the first table, and then shift-select the last table to select all tables. With all tables selected, select **Load**. 

    > It will take a few minutes for the process to complete.

### Task 2: Create a custom report using Power BI and Intune Data Warehouse

1. In the **Visualizations** pane, select the **Treemap** option (the icon appears to have several rectangles of various sizes). The Treemap chart will be added to the report canvas.

2. In the menu bar, select **View**, and then in the ribbon select **Page view** and then select **Actual size**.

3. In the **Fields** pane, find the **devices** table and expand it. 

4. Select the **deviceName** data field and drag it onto the Treemap chart in the report canvas.

5. Drag the **deviceKey** data field from the devices table to the **Visualizations** pane and drop it on under the **Values** section in the box labeled **Add data fields here**.

6. In the Fields pane, scroll down and find the **users** table and expand it. 

7. Drag the **displayName** data field from the users table to the **Visualizations** pane and drop it on under the **Details** section.

   _Note: You should now see device names in each report object, with a user name listed under each device._

8. Select the **Treemap** you added to the report canvas. In the **Visualizations** pane, select the **Table** report option (the icon appears as a spreadsheet) to switch the report canvas to a table view.

9. Select **File**, select **Export**, then select **Export to PDF**. The browser should launch and display the report in a PDF format. 

10. Close all open windows.

11. Sign out of SEA-CL1.

**Results**: After completing this exercise, you will have successfully connected Power BI desktop to the Intune Data Warehouse and created a report using Power BI.


**END OF LAB**
