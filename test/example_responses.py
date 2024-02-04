EXAMPLE_RESPONSE = {
    "serial_number": "1234",
    "total_meter_reading_count": 28000,
    "total_watt_hours": 124000,
    "total_cost": 325,
    "first_reading_timestamp": 1615521060,
    "last_reading_timestamp": 1632810120,
    "last_reading_watt_hours": 2,
    "last_reading_cost": 0.0011875,
    "available_days": 200
}

EXAMPLE_TIME_SERIES_RESPONSE = [
  {
    "timestamp": 1706362080,
    "pulses": 12,
    "watt_hours": 12,
    "cost": 0.0030752332,
    "usage_cost": 0.0022044,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  },
  {
    "timestamp": 1706362140,
    "pulses": 13,
    "watt_hours": 13,
    "cost": 0.0032589333,
    "usage_cost": 0.0023881001,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  }
]

EXAMPLE_TIME_SERIES_START_ONLY_RESPONSE = [
  {
    "timestamp": 1706321820,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.0008708333,
    "usage_cost": 0,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  },
  {
    "timestamp": 1706321880,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.0008708333,
    "usage_cost": 0,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  },
  {
    "timestamp": 1706321940,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.0008708333,
    "usage_cost": 0,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  }
]

EXAMPLE_TIME_SERIES_END_ONLY_RESPONSE = [
  {
    "timestamp": 1706321820,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.0008708333,
    "usage_cost": 0,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  },
  {
    "timestamp": 1706321880,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.0008708333,
    "usage_cost": 0,
    "fixed_cost": 0.0008708333,
    "cost_per_kwh": 0.1837,
    "is_peak": False,
    "is_final": False,
    "samples": 1
  }
]

EXAMPLE_TIME_SERIES_START_END_RESPONSE = [
    {
        "timestamp": 1706321700,
        "pulses": 0,
        "watt_hours": 0,
        "cost": 0.0008708333,
        "usage_cost": 0,
        "fixed_cost": 0.0008708333,
        "cost_per_kwh": 0.1837,
        "is_peak": False,
        "is_final": False,
        "samples": 1
    },
    {
        "timestamp": 1706321760,
        "pulses": 0,
        "watt_hours": 0,
        "cost": 0.0008708333,
        "usage_cost": 0,
        "fixed_cost": 0.0008708333,
        "cost_per_kwh": 0.1837,
        "is_peak": False,
        "is_final": False,
        "samples": 1
    },
    {
        "timestamp": 1706321820,
        "pulses": 0,
        "watt_hours": 0,
        "cost": 0.0008708333,
        "usage_cost": 0,
        "fixed_cost": 0.0008708333,
        "cost_per_kwh": 0.1837,
        "is_peak": False,
        "is_final": False,
        "samples": 1
    },
    {
        "timestamp": 1706321880,
        "pulses": 0,
        "watt_hours": 0,
        "cost": 0.0008708333,
        "usage_cost": 0,
        "fixed_cost": 0.0008708333,
        "cost_per_kwh": 0.1837,
        "is_peak": False,
        "is_final": False,
        "samples": 1
    }
]

EXAMPLE_TIME_SERIES_START_END_SAMPLE_60_RESPONSE = [
  {
    "timestamp": 1706321820,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.18369992,
    "is_peak": False,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706325420,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706329020,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  }
]

EXAMPLE_TIME_SERIES_START_SAMPLE_60_RESPONSE = [
  {
    "timestamp": 1706321820,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.18369992,
    "is_peak": False,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706325420,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706329020,
    "pulses": 0,
    "watt_hours": 0,
    "cost": 0.05225004,
    "usage_cost": 0,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706332620,
    "pulses": 12,
    "watt_hours": 12,
    "cost": 0.056830436,
    "usage_cost": 0.004580397,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  },
]

EXAMPLE_TIME_SERIES_SAMPLE_60_RESPONSE = [
  {
    "timestamp": 1706429160,
    "pulses": 343,
    "watt_hours": 343,
    "cost": 0.18317313,
    "usage_cost": 0.13092309,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.3817,
    "is_peak": True,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706432760,
    "pulses": 377,
    "watt_hours": 377,
    "cost": 0.121504895,
    "usage_cost": 0.06925486,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.18369992,
    "is_peak": False,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706436360,
    "pulses": 884,
    "watt_hours": 884,
    "cost": 0.21464081,
    "usage_cost": 0.16239077,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.18369992,
    "is_peak": False,
    "is_final": False,
    "samples": 60
  },
  {
    "timestamp": 1706439960,
    "pulses": 589,
    "watt_hours": 589,
    "cost": 0.1604493,
    "usage_cost": 0.10819925,
    "fixed_cost": 0.05225004,
    "cost_per_kwh": 0.18369992,
    "is_peak": False,
    "is_final": False,
    "samples": 60
  }
]
