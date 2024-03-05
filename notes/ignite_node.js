const jdbc = require('jdbc');

// JDBC URL for Ignite
const jdbcUrl = 'jdbc:ignite:thin://localhost:10800/';

// Configure the JDBC connection
const config = {
  libpath: 'ignite-core-2.10.0.jar', // Adjust the jar file based on your Ignite version
  drivername: 'org.apache.ignite.IgniteJdbcThinDriver',
  url: jdbcUrl,
  user: 'ignite',
  password: 'ignite',
};

// Establish the JDBC connection
const conn = new jdbc(config);

// Execute SQL query to get table names (caches in Ignite)
conn.initialize(() => {
  conn.open((err, conn) => {
    if (err) {
      console.error(err);
      return;
    }

    conn.createStatement((err, statement) => {
      if (err) {
        console.error(err);
        return;
      }

      statement.executeQuery('SHOW TABLES', (err, resultset) => {
        if (err) {
          console.error(err);
          return;
        }

        // Fetch and print the results
        resultset.toObjArray((err, results) => {
          if (err) {
            console.error(err);
            return;
          }

          results.forEach(row => {
            console.log('Cache Name:', row[0]);
          });

          // Close the statement and connection
          statement.close((err) => {
            if (err) {
              console.error(err);
            }
            conn.close((err) => {
              if (err) {
                console.error(err);
              }
            });
          });
        });
      });
    });
  });
});
