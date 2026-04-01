diff --git a/api/test_server.py b/api/test_server.py
new file mode 100644
index 0000000000000000000000000000000000000000..8deb79db177c76ac7b67d7aaa1989d9e8037f087
--- /dev/null
+++ b/api/test_server.py
@@ -0,0 +1,41 @@
+import unittest
+
+from api import server
+
+
+class TriageTests(unittest.TestCase):
+    def test_specific_rule_matches_before_fallback(self):
+        out = server.evaluate_triage("кървене", ["обилно"])
+        self.assertEqual(out["risk"], "red")
+
+    def test_fallback_rule_for_known_symptom(self):
+        out = server.evaluate_triage("кървене", [])
+        self.assertEqual(out["risk"], "yellow")
+
+    def test_unknown_symptom_returns_yellow(self):
+        out = server.evaluate_triage("случаен симптом", [])
+        self.assertEqual(out["risk"], "yellow")
+
+
+class PayloadValidationTests(unittest.TestCase):
+    def test_reject_invalid_trimester(self):
+        payload = {
+            "title": "x",
+            "slug": "x",
+            "trimester": "invalid",
+            "category": "symptoms",
+            "summary": "x",
+            "body": "x",
+            "when_to_call_doctor": "x",
+            "emergency": "x",
+            "author_name": "x",
+            "author_specialty": "x",
+            "medical_reviewer": "x",
+            "status": "draft",
+        }
+        with self.assertRaises(ValueError):
+            server.validate_payload(payload)
+
+
+if __name__ == "__main__":
+    unittest.main()
