import base64, codecs
magic = 'ZnJvbSBtaXRtcHJveHkgaW1wb3J0IGh0dHANCmltcG9ydCBqc29uDQoNCmRlZiByZXF1ZXN0KGZsb3c6IGh0dHAuSFRUUEZsb3cpIC0+IE5vbmU6DQogICAgaWYgZmxvdy5yZXF1ZXN0LnByZXR0eV91cmwgPT0gImh0dHBzOi8vbGljZW5zZS5zb25pY3dpcmUuY29tLyI6DQogICAgICAgICAgICBmbG93LnJlc3BvbnNlID0gaHR0cC5SZXNwb25zZS5tYWtlKA0KICAgICAgICAgICAgICAgIDIwMCwgDQogICAgICAgICAgICAgICAgYidJRCA6IE1ZT0hBPGJyPlBhc3Nvd3JkIDogTVlPSEEvUGlhcHJvX05UX0J5cGFzczxicj48YSBocmVmPSJodHRwczovL2dpdGh1Yi5jb20vTVlPSEEvUGlhcHJvX05UX0J5cGFzcyI+R2l0SHViPC9hPicsDQogICAgICAgICAgICAgICAgeyJDb250ZW50LVR5cGUiOiAidGV4dC9odG1sIn0gDQogICAgICAgICAgICApDQoNCiAgICBpZiBmbG93LnJlcXVlc3QucHJldHR5X3VybCA9PSAiaHR0cHM6Ly9saWNlbnNlLnNvbmljd2lyZS5jb20vdjEvdG9rZW5zIjoNCiAgICAgICAgZW1haWwgPSBqc29uLmxvYWRzKGZsb3cucmVxdWVzdC5jb250ZW50KVsnZW1haWwnXQ0KICAgICAgICBwYXNzd29yZCA9IGpzb24ubG9hZHMoZmxvdy5yZXF1ZXN0LmNvbnRlbnQpWydwYXNzd29yZCddDQoNCiAgICAgICAgaWYgZW1haWwgPT0gJ01ZT0hBJyBhbmQgcGFzc3dvcmQgPT0gJ01ZT0hBL1BpYXByb19OVF9CeXBhc3MnOg0KICAgICAgICAgICAgZmxvdy5yZXNwb25zZSA9IGh0dHAuUmVzcG9uc2UubWFrZSgNCiAgICAgICAgICAgICAgICAyMDAsICANCiAgICAgICAgICAgICAgICBiJ3sic3RhdHVzIjoib2siLCJhY2Nlc3NfdG9rZW4iOiJCeXBhc3NfTlQifScsDQogICAgICAgICAgICAgICAgeyJDb250ZW50LVR5cGUiOiAidGV4dC9odG1sIn0gIA0KICAgICAgICAgICAgKQ0KDQogICAgaWYgZmxvdy5yZXF1ZXN0LnByZXR0eV91cmwgPT0gImh0dHBzOi8vbGljZW5zZS5zb25pY3dpcmUuY29tL3YxL215L2FjdGl2YXRpb25zIjoNCiAgICAgICAgaWYgZmxvdy5yZXF1ZXN0Lm1ldGhvZCA9PSAiR0VUIjoNCiAgICAgICAgICAgIGZsb3cucmVzcG9uc2UgPSBodHRwLlJlc3BvbnNlLm1ha2UoDQogICAgICAgICAgICAgICAgMjAwLCAgDQogICAgICAgICAgICAgICAgYid7InN0YXR1cyI6Im9rIiwiYWN0aXZhdGlvbnMiOlt7ImlkIjoyODI2LCJ1c2VyX2NvbXBvbmVudF9pZCI6ODk3MywiZGV2aWNlX2lkIjoyNzc2LCJhY3RpdmF0ZWQiOjEsInVwZGF0ZV9jb3VudCI6MCwiY3JlYXRlZF9hdCI6IjIwMjAtMTItMTkgMDM6NDU6NTAiLCJ1cGRhdGVkX2F0IjoiMjAyMC0xMi0xOSAwMzo0NTo1MCIsInVzZXJfY29tcG9uZW50Ijp7ImlkIjo4OTczLCJ1c2VyX2lkIjo1MjQ3NDgsImNvbXBvbmVudF9pZCI6MSwiYWN0aXZhdGlvbl9saW1pdCI6MywiZGlzYWJsZWQiOjAsImNyZWF0ZWRfYXQiOiIyMDIwLTEyLTE5IDAzOjE2OjEyIiwidXBkYXRlZF9hdCI6IjIwMjAtMTItMTkgMDM6MTY6MTIiLCJjb21wb25lbnQiOnsiaWQiOjEsInJlc291cmNlX2lkIjoiRTAxNjhBNTQtQzQzMS00NjgyLThDMzgtQUUxNDFCQzBGOTk0IiwibmFtZSI6IkhBVFNVTkUgTUlLVSBOVCBPcmlnaW5hbCIsImZpbGVfbmFtZSI6Im1pa3VudCIsImFjdGl2YXRpb25fbGltaXQiOjMsInJhbmsiOjEwMCwiY3JlYXRlZF9hdCI6IjIwMjAtMDItMTggMTM6NTI6MDYiLCJ1cGRhdGVkX2F0IjoiMjAyMC0wMi0xOCAxMzo1MjowNiJ9fX0seyJpZCI6MTM4MDEsInVzZXJfY29tcG9uZW50X2lkIjo4OTczLCJkZXZpY2VfaWQiOjc1NDUsImFjdGl2YXRlZCI6MSwidXBkYXRlX2NvdW50IjowLCJjcmVhdGVkX2F0IjoiMjAyMS0xMi0wNSAxNzozMjowNCIsInVwZGF0ZWRfYXQiOiIyMDIxLTEyLTA1IDE3OjMyOjA0IiwidXNlcl9jb21wb25lbnQiOnsiaWQiOjg5NzMsInVzZXJfaWQiOjUyNDc0OCwiY29tcG9uZW50X2lkIjoxLCJhY3RpdmF0aW9uX2xpbWl0IjozLCJkaXNhYmxlZCI6MCwiY3JlYXRlZF9hdCI6IjIwMjAtMTItMTkgMDM6MTY6MTIiLCJ1cGRhdGVkX2F0IjoiMjAyMC0xMi0xOSAwMzoxNjoxMiIsImNvbXBvbmVudCI6eyJpZCI6MSwicmVzb3VyY2VfaWQiO'
love = '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'
god = '50X2lkIjozLCJhY3RpdmF0aW9uX2xpbWl0IjozLCJkaXNhYmxlZCI6MCwiY3JlYXRlZF9hdCI6IjIwMjAtMTItMTkgMDM6MTY6MTIiLCJ1cGRhdGVkX2F0IjoiMjAyMC0xMi0xOSAwMzoxNjoxMiIsImNvbXBvbmVudCI6eyJpZCI6MywicmVzb3VyY2VfaWQiOiJDMDdEMTk4RS0wNTc3LTRENzktODE0Qy1EQjZBNUE5RjA2Q0EiLCJuYW1lIjoiSEFUU1VORSBNSUtVIE5UIERhcmsiLCJmaWxlX25hbWUiOiJtaWt1bnQiLCJhY3RpdmF0aW9uX2xpbWl0IjozLCJyYW5rIjozMDAsImNyZWF0ZWRfYXQiOiIyMDIwLTExLTE4IDExOjAwOjI2IiwidXBkYXRlZF9hdCI6IjIwMjAtMTEtMTggMTE6MDA6MjYifX19XX0nLCAgDQogICAgICAgICAgICAgICAgeyJDb250ZW50LVR5cGUiOiAidGV4dC9odG1sIn0gIA0KICAgICAgICAgICAgKQ0KDQogICAgICAgIGlmIGZsb3cucmVxdWVzdC5tZXRob2QgPT0gIlBPU1QiOg0KICAgICAgICAgICAgZGV2aWNlX3Jlc291cmNlX2lkID0ganNvbi5sb2FkcyhmbG93LnJlcXVlc3QuY29udGVudClbJ2RldmljZV9yZXNvdXJjZV9pZCddDQogICAgICAgICAgICBkZXZpY2VfbmFtZSA9IGpzb24ubG9hZHMoZmxvdy5yZXF1ZXN0LmNvbnRlbnQpWydkZXZpY2VfbmFtZSddDQogICAgICAgICAgICBkZXZpY2VfdmVyc2lvbiA9IGpzb24ubG9hZHMoZmxvdy5yZXF1ZXN0LmNvbnRlbnQpWydkZXZpY2VfdmVyc2lvbiddDQogICAgICAgICAgICBwb3N0ID0gJ3sic3RhdHVzIjoib2siLCJhY3RpdmF0aW9uX3Jlc3VsdHMiOlt7ImNvbXBvbmVudF9yZXNvdXJjZV9pZCI6IjI1RTJFQkVDLTlBRTQtNDBCQi1BMEE5LUZBQkZEQjlBMkFGMCIsImRldmljZV9yZXNvdXJjZV9pZCI6ImNoYW5nZV9kZXZpY2VfcmVzb3VyY2VfaWQiLCJkZXZpY2VfbmFtZSI6ImNoYW5nZV9kZXZpY2VfbmFtZSIsImRldmljZV92ZXJzaW9uIjoiY2hhbmdlX2RldmljZV92ZXJzaW9uIiwicmVzdWx0IjoiQWN0aXZhdGVkIiwiYWN0aXZhdGVkX2NvdW50IjozLCJhY3RpdmF0aW9uIjp7InVzZXJfY29tcG9uZW50X2lkIjo4OTc0LCJkZXZpY2VfaWQiOjgwMTYsImFjdGl2YXRlZCI6MSwidXBkYXRlX2NvdW50IjowLCJjcmVhdGVkX2F0IjoiMjAyMi0wMS0xNSAxMDo0MzoxOSIsInVwZGF0ZWRfYXQiOiIyMDIyLTAxLTE1IDEwOjQzOjE5IiwiaWQiOjE1NDI5LCJ1c2VyX2NvbXBvbmVudCI6eyJpZCI6ODk3NCwidXNlcl9pZCI6NTI0NzQ4LCJjb21wb25lbnRfaWQiOjIsImFjdGl2YXRpb25fbGltaXQiOjMsImRpc2FibGVkIjowLCJjcmVhdGVkX2F0IjoiMjAyMC0xMi0xOSAwMzoxNjoxMiIsInVwZGF0ZWRfYXQiOiIyMDIwLTEyLTE5IDAzOjE2OjEyIiwiY29tcG9uZW50Ijp7ImlkIjoyLCJyZXNvdXJjZV9pZCI6IjI1RTJFQkVDLTlBRTQtNDBCQi1BMEE5LUZBQkZEQjlBMkFGMCIsIm5hbWUiOiJIQVRTVU5FIE1JS1UgTlQgV2hpc3BlciIsImZpbGVfbmFtZSI6Im1pa3VudCIsImFjdGl2YXRpb25fbGltaXQiOjMsInJhbmsiOjIwMCwiY3JlYXRlZF9hdCI6IjIwMjAtMTEtMTggMTE6MDA6MDciLCJ1cGRhdGVkX2F0IjoiMjAyMC0xMS0xOCAxMTowMDowNyJ9fSwiZGV2aWNlIjp7ImlkIjo4MDE2LCJyZXNvdXJjZV9pZCI6ImNoYW5nZV9kZXZpY2VfcmVzb3VyY2VfaWQiLCJuYW1lIjoiY2hhbmdlX2RldmljZV9uYW1lIiwidmVyc2lvbiI6ImNoYW5nZV9kZXZpY2VfdmVyc2lvbiIsImNyZWF0ZWRfYXQiOiIyMDIyLTAxLTE1IDEwOjQzOjE5IiwidXBkYXRlZF9hdCI6IjIwMjItMDEtMTUgMTA6NDM6MTkifX19LHsiY29tcG9uZW50X3Jlc291cmNlX2lkIjoiQzA3RDE5OEUtMDU3Ny00RDc5LTgxNEMtREI2QTVBOUYwNkNBIiwiZGV2aWNlX3Jlc291cmNlX2lkIjoiY2hhbmdlX2RldmljZV9yZXNvdXJjZV9pZCIsImRldmljZV9uYW1lIjoiY2hhbmdlX2RldmljZV9uYW1lIiwiZGV2aWNlX3ZlcnNpb24iOiJjaGFuZ2VfZGV2aWNlX3ZlcnNpb24iLCJyZXN1bHQiOiJBY3RpdmF0ZWQiLCJhY3RpdmF0ZWRfY291bnQiOjMsImFjdGl2YXRpb24iOnsidXNlcl9jb21wb25lbnRfaWQiOjg5NzUsImRldmljZV9pZCI6ODAxNiwiYWN0aXZhdGVkIjoxLCJ1cGRhdGVfY29'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))