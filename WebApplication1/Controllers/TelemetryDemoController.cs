﻿//using Microsoft.AspNetCore.Mvc;

//namespace WebApplication1.Controllers
//{
//    public class TelemetryDemoController : Controller
//    {
//        public IActionResult Index()
//        {
//            return View();
//        }
//    }
//}

using Microsoft.AspNetCore.Mvc;
using Microsoft.ApplicationInsights;
using Microsoft.ApplicationInsights.DataContracts;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class TelemetryDemoController : ControllerBase
{
    private readonly TelemetryClient _telemetryClient;

    public TelemetryDemoController(TelemetryClient telemetryClient)
    {
        _telemetryClient = telemetryClient;
    }

    // VERBOSE TRACE
    [HttpGet("trace-verbose")]
    public IActionResult LogVerbose()
    {
        _telemetryClient.TrackTrace("This is a VERBOSE log", SeverityLevel.Verbose);
        return Ok("Verbose log sent");
    }

    // Sample Log Output (JSON blob-style)
    /*
    {
      "message": "This is a VERBOSE log",
      "severityLevel": "Verbose",
      "timestamp": "2025-03-21T14:20:00Z",
      "type": "Trace"
    }
    */

    // INFORMATION TRACE
    [HttpGet("trace-info")]
    public IActionResult LogInfo()
    {
        _telemetryClient.TrackTrace("This is an INFORMATION log", SeverityLevel.Information);
        return Ok("Information log sent");
    }

    /*
    {
      "message": "This is an INFORMATION log",
      "severityLevel": "Information",
      "timestamp": "2025-03-21T14:21:00Z",
      "type": "Trace"
    }
    */

    // WARNING TRACE
    [HttpGet("trace-warning")]
    public IActionResult LogWarning()
    {
        _telemetryClient.TrackTrace("This is a WARNING log", SeverityLevel.Warning);
        return Ok("Warning log sent");
    }

    /*
    {
      "message": "This is a WARNING log",
      "severityLevel": "Warning",
      "timestamp": "2025-03-21T14:22:00Z",
      "type": "Trace"
    }
    */

    // EXCEPTION
    [HttpGet("log-exception")]
    public IActionResult LogException()
    {
        try
        {
            int fail = 0;
            int result = 10 / fail;
        }
        catch (Exception ex)
        {
            _telemetryClient.TrackException(ex);
        }
        return Ok("Exception logged");
    }

    /*
    {
      "type": "Exception",
      "exception": {
        "message": "Attempted to divide by zero.",
        "type": "System.DivideByZeroException",
        "stackTrace": "at TelemetryDemoController.LogException()..."
      },
      "severityLevel": "Error",
      "timestamp": "2025-03-21T14:23:00Z"
    }
    */

    // CUSTOM EVENT
    [HttpGet("log-event")]
    public IActionResult LogEvent()
    {
        _telemetryClient.TrackEvent("UserSignedUp", new Dictionary<string,string>
        {
            { "Plan", "Premium" },
            { "Region", "East US" }
        });

        return Ok("Custom event logged");
    }

    /*
    {
      "type": "Event",
      "name": "UserSignedUp",
      "properties": {
        "Plan": "Premium",
        "Region": "East US"
      },
      "timestamp": "2025-03-21T14:24:00Z"
    }
    */

    // DEPENDENCY
    [HttpGet("log-dependency")]
    public IActionResult LogDependency()
    {
        _telemetryClient.TrackDependency("SQL", "GetUsers", "SELECT * FROM Users", DateTimeOffset.Now, TimeSpan.FromMilliseconds(200), true);
        return Ok("Dependency logged");
    }

    /*
    {
      "type": "Dependency",
      "target": "SQL",
      "name": "GetUsers",
      "data": "SELECT * FROM Users",
      "duration": "00:00:00.200",
      "success": true,
      "timestamp": "2025-03-21T14:25:00Z"
    }
    */

    // REQUEST
    [HttpGet("log-request")]
    public IActionResult LogRequest()
    {
        _telemetryClient.TrackRequest("HomePageRequest", DateTimeOffset.Now, TimeSpan.FromMilliseconds(150), "200", true);
        return Ok("Request telemetry logged");
    }

    /*
    {
      "type": "Request",
      "name": "HomePageRequest",
      "duration": "00:00:00.150",
      "responseCode": "200",
      "success": true,
      "timestamp": "2025-03-21T14:26:00Z"
    }
    */

}
