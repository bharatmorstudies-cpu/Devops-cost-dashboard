import datetime
import boto3
from botocore.exceptions import ClientError


def get_aws_costs():
    """Fetches total AWS costs for the last 30 days grouped by service."""
    try:
        # Initialize the Cost Explorer client
        # Note: Cost Explorer API endpoint is always us-east-1
        ce_client = boto3.client("ce", region_name="us-east-1")

        # Set up date range (Last 30 days)
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=30)

        print(f"--- Fetching AWS Costs from {start_date} to {end_date} ---")

        response = ce_client.get_cost_and_usage(
            TimePeriod={
                "Start": start_date.strftime("%Y-%m-%d"),
                "End": end_date.strftime("%Y-%m-%d"),
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],
        )

        for result in response.get("ResultsByTime", []):
            print(f"\nTime Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}")
            print("-" * 40)
            for group in result.get("Groups", []):
                service_name = group["Keys"][0]
                amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
                unit = group["Metrics"]["UnblendedCost"]["Unit"]
                if amount > 0.0:  # Only show services that actually cost money
                    print(f"Service: {service_name:<30} Cost: {amount:.2f} {unit}")

    except ClientError as e:
        print(f"Error fetching billing data: {e}")


def get_cloudwatch_metrics():
    """Fetches general EC2 CPU utilization metrics from CloudWatch as a test."""
    try:
        # Initialize CloudWatch client (Change region to match your resources)
        cw_client = boto3.client("cloudwatch", region_name="us-east-1")

        print("\n--- Fetching CloudWatch Metrics (EC2 CPU Utilization Test) ---")

        # Set up timeframe for the last 24 hours
        end_time = datetime.datetime.now(datetime.timezone.utc)
        start_time = end_time - datetime.timedelta(hours=24)

        response = cw_client.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            StartTime=start_time,
            EndTime=end_time,
            Period=3600,  # 1-hour intervals
            Statistics=["Average"],
            Unit="Percent",
        )

        datapoints = response.get("Datapoints", [])
        if not datapoints:
            print("No EC2 CPU data found in this timeframe or region.")
            return

        # Sort datapoints chronologically
        datapoints.sort(key=lambda x: x["Timestamp"])
        for dp in datapoints:
            print(f"Time: {dp['Timestamp'].strftime('%Y-%m-%d %H:%M')} | Average CPU: {dp['Average']:.2f}%")

    except ClientError as e:
        print(f"Error fetching CloudWatch data: {e}")


if __name__ == "__main__":
    get_aws_costs()
    get_cloudwatch_metrics()
