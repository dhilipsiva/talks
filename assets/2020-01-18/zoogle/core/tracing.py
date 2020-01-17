from opentelemetry import trace
from opentelemetry.ext import jaeger
# from opentelemetry.context import Context
from opentelemetry.sdk.trace import TracerSource
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

trace.set_preferred_tracer_source_implementation(lambda T: TracerSource())
trace.tracer_source().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)
tracer = trace.tracer_source().get_tracer(__name__)

# create a JaegerSpanExporter
jaeger_exporter = jaeger.JaegerSpanExporter(
    service_name='zoogle',
    # configure agent
    agent_host_name='jaeger',
    agent_port=6831,
    # optional: configure also collector
    collector_host_name='jaeger',
    collector_port=14268,
    collector_endpoint='/api/traces?format=jaeger.thrift',
    # username=xxxx, # optional
    # password=xxxx, # optional
)

# Create a BatchExportSpanProcessor and add the exporter to it
span_processor = BatchExportSpanProcessor(jaeger_exporter)

# add to the tracer
tracer.add_span_processor(span_processor)
