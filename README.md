# wwwsqldesigner-aws

Custom backend to store `wwwsqldesigner` models on S3, using lambda functions.

## Required environment variables

* `S3_BUCKET`: the bucket in which to store the database designs. Must already exist.

## How to deploy

```bash
npm install
serverless deploy
```

## TODO

* Deploy `wwwsqldesigner` to S3 static website hosting;
* Add authentication;
* Add authorization.

## License

MIT
