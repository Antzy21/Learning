using StackExchange.Redis;

void SaveDataToRedisDb(IDatabase db)
{
    var examples = new Dictionary<string, string>
    {
        { "Key0", "MyString0" },
        { "Key1", "MyString1" },
        { "Key2", "MyString2" },
        { "Key3", "MyString3" }
    };

    foreach (var (key, value) in examples)
    {
        if (db.StringSet(key, value))
        {
            Console.WriteLine($"Successfully set {key}, {value}");
        }
        else
        {
            Console.WriteLine($"Unable to set {key}, {value}");
        }
    }
}

/// **************
/// This is redis config to connect to a docker image.
/// The image is running on a specific port locally.
/// **************
var config = new ConfigurationOptions()
{
    AllowAdmin = true,
    EndPoints = { "localhost:6379" }
};

// Make the connection with the config.
ConnectionMultiplexer redis = ConnectionMultiplexer.Connect(config);

var db = redis.GetDatabase();

// Endpoints are individual redis instances (could be multiple in other docker containers I think(
var endpoints = redis.GetEndPoints();
// Get the server on the endpoint. (We only have one endpoint, so use Single() here)
var server = redis.GetServer(endpoints.Single());
// Get all the keys!
var keys = server.Keys();

// Deletes all the entries in database 0, on the server
server.FlushDatabase(0);

// Save some example strings to the redis db.
SaveDataToRedisDb(db);

Console.WriteLine($"\nNumber of keys: {keys.Count()}\n");

foreach (var key in keys)
{
    Console.WriteLine($"{key}, {db.StringGet(key)}");
}