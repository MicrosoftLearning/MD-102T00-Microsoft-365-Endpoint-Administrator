---
title: Get started with the MD-102 labs
---

# Get started with the MD-102 labs

These labs give you hands-on practice managing and securing Microsoft 365 endpoints with Microsoft Intune. They run in one Microsoft 365 tenant, and each lab builds on the configuration from the labs before it.

## Your lab environment

| Item | Detail |
| --- | --- |
| Tenant | A Microsoft 365 tenant for the Contoso scenario. Lab steps show its domain as `<TenantPrefix>.onmicrosoft.com`. |
| SEA-DEV1 | An enrolled Windows device with Megan Bowen signed in. You do most administration, Microsoft Graph PowerShell, and app packaging work here. |
| SEA-DEV2 | An enrolled Windows device with Joni Sherman signed in. |
| SEA-DEV3 | A Windows device for Windows Autopilot registration and Endpoint Privilege Management testing. |
| LIN-SRV1 | An Ubuntu server for Microsoft Tunnel Gateway in Lab 04. |
| Lab files | The read-only **AllFiles (F:)** drive on the Windows VMs. |

> [!NOTE]
> Sign in with the accounts and passwords provided in your lab environment. Replace `<TenantPrefix>` in lab steps with your tenant's prefix.

## Lab files

The **AllFiles (F:)** drive holds the files you use in the labs, such as the Group Policy backup and the remediation scripts in Lab 02. The drive is read-only, so copy a file before you edit it. If you aren't using the hosted lab environment, each step that uses a file links to it so you can download it from this repo's [Allfiles](https://github.com/MicrosoftLearning/MD-102T00-Microsoft-365-Endpoint-Administrator/tree/main/Allfiles) folder.

## How the labs work

- **Start with Lab 01.** It's the foundational lab. It sets up identity, enrollment, and the free 90-day Intune Suite trial that later labs use, and every later lab assumes it's complete.
- **Expect sync delays.** Policies, apps, and device status can take minutes to hours to apply. Force a device sync when a lab suggests it. Endpoint analytics and Advanced Analytics need 24 to 48 hours of device telemetry, and Microsoft Defender for Endpoint provisioning can take several hours.
- **Each exercise ends with a result you can check.** Confirm it before you move on, because later exercises build on it.

## The labs

{% assign course = site.data.course %}
{% for section in course.sections %}{% for group in section.groups %}
**{{ group.title }}**

{% for item in group.items %}- [{{ item.title }}]({{ item.url | relative_url }}){% if item.minutes %} ({{ item.minutes }} minutes){% endif %}
{% endfor %}
{% endfor %}{% endfor %}
When you're ready, start with Lab 01.
