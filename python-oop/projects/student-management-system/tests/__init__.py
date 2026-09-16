"""
SMS Unit Tests Package
Ensures project root is added to sys.path for test discovery from any directory.
"""
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
