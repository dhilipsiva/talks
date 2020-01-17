from opentelemetry import metrics
from opentelemetry.sdk.metrics import Counter, Meter
from opentelemetry.sdk.metrics.export import ConsoleMetricsExporter

metrics.set_preferred_meter_implementation(lambda T: Meter())
meter = metrics.meter()
exporter = ConsoleMetricsExporter()

counter = meter.create_metric(
    "available memory",
    "available memory",
    "bytes",
    int,
    Counter,
    ("environment",),
)

label_values = ("staging",)
counter_handle = counter.get_handle(label_values)
counter_handle.add(100)

exporter.export([(counter, label_values)])
exporter.shutdown()
