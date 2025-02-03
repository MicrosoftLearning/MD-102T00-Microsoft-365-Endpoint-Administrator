# Practice Lab01: Configure Windows Devices in Intune

## Summary

In this lab, you use Group Policy Analytics to import an Active Directory Group Policy Object (GPO) and identify settings that support equivalent Microsoft Intune MDM policy.

### Scenario

Contoso has traditionally used Active Directory GPOs to deploy computer and user policy settings throughout the domain. You plan to move all supported GPO settings to Microsoft Intune configuration profiles. You have a GPO named **Windows Client Policy**. You need to use Group Policy Analytics to validate the settings in the Windows Client Policy GPO and identify which settings can be successfully migrated into Intune.

### Task 1: Analyze the Windows Client GPO using Group Policy Analytics

1. Log on to **MD102-WS1** and, if necessary, sign in as **Contoso\Administrator** with the password of **Pa55w.rd**.

1. On **MD102-WS1**, on the taskbar, select **Microsoft Edge**.

2. In Microsoft Edge, type **https://intune.microsoft.com** in the address bar, and then press **Enter**. 

3. Sign in as **`admin@yourtenant.onmicrosoft.com`** with the tenant Admin password.

4. In the Microsoft Intune admin center, in the navigation pane, select **Devices**.

5. On the **Devices | Overview** page, in the **Manage devices** section, select **Group Policy analytics**.

6. On the **Devices | Group Policy analytics** blade, select **Import**.

7. On the Import GPO files page, click the **Select a file** button.

8. In the **Open** box, select **Documents** and then select **Windows Client Policy.xml**. Select **Open**.

   > The Windows Client Policy GPO is immediately imported and analyzed.

9. Select Next twice, then select **Create**.

   > The Windows Client Policy GPO is imported and analyzed. It may take a few minutes to complete.

10. Close the **Import GPO files** page.

11. On the **Devices | Group Policy analytics** blade, review the information next to **Windows Client Policy**.

    > Notice that 89% of the settings have MDM support.

12. Under MDM Support, select **89%**. 

    > Notice each **Setting Name**, **MDM Support**, **CSP name**, and the **CSP mapping** for each supported setting. Take note of which settings do not have an equivalent CSP mapping.

### Task 2: Review the Group Policy Analytics Summary Report

1. In the Microsoft Intune admin center, in the navigation pane, select **Reports**.

2. On the **Reports** page, in the **Device management** section, select **Group Policy analytics**.

3. In the details pane, under **Summary**, select **Refresh**.

   > It may take several minutes to refresh and build the summary report. You may need to refresh several times.

4. Review the **Group policy migration readiness** information.

   > There should be a number of policies ready for migration and a number of policies not supported.

5. On the **Reports | Group policy analytics** blade, select **Reports** tab, and then select **Group policy migration readiness**.

   > The Group policy migration readiness report provides information related to each setting, and the Profile Type supported.

6. Select **Generate again**. 

7. The Group policy migration readiness report provides information related to each setting, and the Profile Type supported.

8. Close the **Group policy migration readiness** window.

9. Close Microsoft Edge.

**Results**: After completing this exercise, you will have successfully exported a GPO and used Group Policy Analytics to validate equivalent policy settings in Intune.

**END OF LAB**
