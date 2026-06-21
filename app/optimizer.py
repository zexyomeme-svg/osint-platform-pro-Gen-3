import psutil
import os
import gc

class ResourceOptimizer:
    def __init__(self, ram_limit_mb=512):
        self.ram_limit_mb = ram_limit_mb

    def get_stats(self):
        # Process-specific memory (RSS = Resident Set Size)
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        process_ram_mb = mem_info.rss / (1024 * 1024)
        
        # System-wide memory (Note: In containers, this might report host RAM)
        sys_mem = psutil.virtual_memory()
        sys_ram_used_mb = sys_mem.used / (1024 * 1024)
        sys_ram_total_mb = sys_mem.total / (1024 * 1024)
        
        # CPU Usage (interval=0.1 gives a real-time snapshot)
        cpu_percent = psutil.cpu_percent(interval=0.1)
        
        # Calculate percentage based on the specific Render Free Tier limit
        # This is the most important stat for the user to avoid OOM
        limit_percent = (process_ram_mb / self.ram_limit_mb) * 100
        
        return {
            "process_ram": round(process_ram_mb, 2),
            "sys_ram_used": round(sys_ram_used_mb, 2),
            "sys_ram_total": round(sys_ram_total_mb, 2),
            "ram_limit": self.ram_limit_mb,
            "ram_percent": round(limit_percent, 2),
            "cpu_usage": cpu_percent,
            "status": "Optimal" if limit_percent < 75 else "Warning" if limit_percent < 90 else "Critical"
        }

    def optimize(self):
        # Force garbage collection to reclaim unused memory
        gc.collect()
        # Optional: Clear any cached data if implemented
        return "Adaptive Memory Cleanup: Garbage collection triggered. Process memory reclaimed."

optimizer = ResourceOptimizer()
