using Microsoft.AspNetCore.Builder;
using static System.Net.WebRequestMethods;


namespace WebApplication1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            //// Enable Application Insights with your connection string
            //builder.Services.AddApplicationInsightsTelemetry(
            //    builder.Configuration["ApplicationInsights:ConnectionString"]);



            // Enable Application Insights with your connection string
            builder.Services.AddApplicationInsightsTelemetry(options =>
            {
                options.ConnectionString = builder.Configuration["ApplicationInsights:ConnectionString"];
            });




            // Add services to the container.
            builder.Services.AddControllersWithViews();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");

            app.Run();
        }
    }
}
//f4f9a77a - ff38 - 4fa1 - 8c5b - 55896575ae98
//InstrumentationKey = f4f9a77a - ff38 - 4fa1 - 8c5b - 55896575ae98; IngestionEndpoint = https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=eb625759-19d2-47dc-acb1-6188c04a60b4